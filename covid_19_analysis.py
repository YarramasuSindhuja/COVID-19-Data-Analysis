# -*- coding: utf-8 -*-
"""COVID-19 Analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TtVoD3S_DXlhF6O1YA7EblAeiCYM0Rcz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
df = pd.read_csv(url)
df.head()

df.describe()

df.isnull().sum()

df = df[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]
df.dropna(inplace=True)

df['date'] = pd.to_datetime(df['date'])

plt.figure(figsize=(12, 6))
sns.lineplot(data=df[df['location'] == 'India'], x='date', y='total_cases', label='India')
sns.lineplot(data=df[df['location'] == 'United States'], x='date', y='total_cases', label='USA')
plt.title("COVID-19 Total Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.show()

df_india = df[df['location'] == 'India'].tail(30)  # Last 30 days
plt.figure(figsize=(12, 6))
sns.barplot(data=df_india, x='date', y='new_cases', color='blue')
plt.xticks(rotation=90)
plt.title("Daily New COVID-19 Cases in India (Last 30 Days)")
plt.show()