# COVID-19 Data Analysis in Google Colab

## This script loads COVID-19 data, cleans it, visualizes trends, and generates a README file.

## Step 1: Install & Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Step 2: Load COVID-19 Dataset
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
df = pd.read_csv(url)

## Step 3: Explore the Data
print("Dataset Preview:")
print(df.head())
print("\nColumn Names:")
print(df.columns)

## Step 4: Select Key Columns
df = df[['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]
df.dropna(inplace=True)  # Remove missing values

## Convert date to datetime format
df['date'] = pd.to_datetime(df['date'])

## Step 5: Data Visualization
## Line Plot - COVID-19 Cases Over Time for Specific Countries
plt.figure(figsize=(12, 6))
sns.lineplot(data=df[df['location'] == 'India'], x='date', y='total_cases', label='India')
sns.lineplot(data=df[df['location'] == 'United States'], x='date', y='total_cases', label='USA')
plt.title("COVID-19 Total Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.show()

## Bar Chart - New Cases for Last 30 Days in India
df_india = df[df['location'] == 'India'].tail(30)  # Last 30 days
plt.figure(figsize=(12, 6))
sns.barplot(data=df_india, x='date', y='new_cases', color='blue')
plt.xticks(rotation=90)
plt.title("Daily New COVID-19 Cases in India (Last 30 Days)")
plt.show()

## Step 6 (Optional): Save README.md File
readme_content = """# COVID-19 Data Insights

### Project Overview
COVID-19 Data Insights is a data-driven project that analyzes the impact of the COVID-19 pandemic using real-world datasets. This project leverages **Python in Google Colab** to explore trends, visualize case progression, and extract meaningful insights.

### Features
✔️ Data collection from trusted sources (e.g., Johns Hopkins, Kaggle, WHO)  
✔️ Exploratory Data Analysis (EDA) to understand trends  
✔️ Visualizations of cases, recoveries, and fatalities  
✔️ Country-wise and global trend comparisons  
✔️ Time-series analysis of COVID-19 spread  
✔️ Machine learning predictions (optional)  

### Technologies Used
- **Python** (Pandas, NumPy, Matplotlib, Seaborn)  
- **Google Colab**  
- **Data Visualization** (Seaborn, Matplotlib)  

### Dataset Sources
- [Our World in Data COVID-19 Dataset](https://ourworldindata.org/coronavirus)

### Setup Instructions
#### 1.Open Google Colab
- Go to [Google Colab](https://colab.research.google.com/) and create a new notebook.

#### 2.Load the Required Libraries
Run the following command in a Colab cell:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
