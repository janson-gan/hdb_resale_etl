import pandas as pd # Loads panda for tables and data wrangling
import matplotlib.pyplot as plt # Loads pyplot for creating plots and visualizations
import seaborn as sns # Loads seaborn for creating informative statistical graphics 
import os # Loads os for file system operations
from pathlib import Path

def run():
    pd.set_option("display.max_columns", None) # To show all columns when printing the dataframe
    project_root = Path(__file__).resolve().parent.parent
    raw_path = project_root/"data"/"raw"/"resale_flat_prices_2017_onwards.csv"
    # raw_path = "../data/raw/resale_flat_prices_2017_onwards.csv" # stores the relative location of the CSV file
    print(os.path.exists(raw_path))  # To check if that path is valid and prints True or False (Expected it to be True)
    df = pd.read_csv(raw_path) # Loads the CSV into a pandas dataframe named df
    print(df.head()) # Shows the first 5 rows for a quick preview

    print(df.info()) # Provides a concise summary of the DataFrame eg 220 174 rows 12 columns non null
    print(df.describe()) # Provides summary statistics for numeric columns eg count, mean, std

    df.isnull().sum().sort_values(ascending=False)

    for col in ['town', 'flat_type', 'flat_model']:
        print(f"{col}:", df[col].nunique(), "unique values")
        print(df[col].unique())
        print()

    df.duplicated().sum()

    df["month"] = pd.to_datetime(df["month"], format="%Y-%m") # Converts the month column from a text eg 2017-01 to a real datetime value eg 2017-01-01
    df["year"] = df["month"].dt.year # Extracts just the numeric year eg 2017
    df["month_num"] = df["month"].dt.month # Extracts month number 1 to 12
    df["year_month"] = df["month"].dt.to_period("M") # Converts to a "Period" type such as 2017-01 for grouping by month

    print(df.head()) # Shows the first 5 rows)

    print(df.info()) # Shows the updated structure after transformation eg 15 columns instead of 12 and new columns are of correct data type

    df["town"].value_counts().head(10) # Gives the frequency of each category and to detect any anomaly

    df["flat_type"].value_counts() # Gives the frequency of each category and to detect any anomaly

    df["flat_model"].value_counts().head(10) # Gives the frequency of each category and to detect any anomaly

    plt.figure(figsize=(8,5))
    sns.histplot(df["resale_price"], kde=True)
    plt.title("Distribution of Resale Prices")
    plt.show()

    df.groupby("year").size().plot(kind="bar", figsize=(8,4))
    plt.title("Transactions per Year")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.show()

    df.groupby("flat_type")["resale_price"].mean().sort_values().plot(
        kind="bar", figsize=(8,4)
    )
    plt.title("Average Resale Price by Flat Type")
    plt.ylabel("Average Price")
    plt.show()

    monthly_avg = df.groupby("year_month")["resale_price"].mean()

    plt.figure(figsize=(12,5))
    monthly_avg.plot()
    plt.title("Average Resale Price Over Time (2017–Present)")
    plt.ylabel("Average Price")
    plt.show()

    df["town"].value_counts().head(10).plot(kind="bar", figsize=(8,4))
    plt.title("Top 10 Towns by Volume")
    plt.show()

    return df