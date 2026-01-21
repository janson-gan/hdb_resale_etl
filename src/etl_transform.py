import pandas as pd
import numpy as np
from datetime import datetime
import re #import regex - Regular Expression Module
from pathlib import Path

def run(df):
    project_root = Path(__file__).resolve().parent.parent
    file_path_get = project_root / "data" / "raw" / "resale_flat_prices_2017_onwards.csv"

    # Load the CSV file
    df = pd.read_csv(file_path_get)

    # Convert month column to proper datetime,%Y in 4-digit year, %m in 2-digit month, - is connect with dash character
    df['month'] = pd.to_datetime(df['month'], format='%Y-%m')

    # Extract year and month separately - generate resale_month, resale_year, resale_quarter column
    df['resale_year'] = df['month'].dt.year
    df['resale_month'] = df['month'].dt.month
    df['resale_quarter'] = df['month'].dt.quarter

    # Clean and standardize remaining_lease column - generate remaining_lease_years column
    def remaining_lease_count(lease_str):
        #Checks if the input is NaN (Not a Number - missing value)
        #If input is missing, immediately return np.nan (a special floating-point value representing missing data)
        if pd.isna(lease_str):  
            return np.nan
        
        # Extract years and months using regex
        #(\d+): Captures one or more digits
        #\s*: Matches zero or more whitespace characters
        #years?: Matches "year" or "years" (the ? makes "s" optional, same goes for months)
        
        years_match = re.search(r'(\d+)\s*years?', str(lease_str))
        months_match = re.search(r'(\d+)\s*months?', str(lease_str))

        #group[0] stands for entire match group - return digit + year / month
        #group[1] stands for first match group - return digit
        #group[2] stands for second match group - return year / month
        #check if return digit, else return 0
        years = int(years_match.group(1)) if years_match else 0
        months = int(months_match.group(1)) if months_match else 0
        
        return round(years + (months/12))

    df['remaining_lease_years'] = df['remaining_lease'].apply(remaining_lease_count)

    # Calculate approximate age of flat - generate flat_ages_years column based on resale year
    df['flat_age_years'] = (df['resale_year'] - df['lease_commence_date'])  # Approximate age based on resale year

    # Calculate price per square meter - generate price_per_sqm column
    df['price_per_sqm'] = df['resale_price'] / df['floor_area_sqm']
    df['price_per_sqm'] = df['price_per_sqm'].round(2)

    # Categorize flats by age - generate flat_age_category column
    def categorize_age(age):
        if age < 10:
            return 'New (<10 years)'
        elif age < 20:
            return 'Young (10-19 years)'
        elif age < 30:
            return 'Middle-aged (20-29 years)'
        elif age < 40:
            return 'Mature (30-39 years)'
        else:
            return 'Old (>39 years)'

    df['flat_age_category'] = df['flat_age_years'].apply(categorize_age)

    # Categorize by price range - generate price_category column
    def categorize_price(price):
        if price < 300000:
            return 'Low (<300k)'
        elif price < 500000:
            return 'Medium (300k-499k)'
        elif price < 800000:
            return 'High (500k-799k)'
        else:
            return 'Premium (>799k)'

    df['price_category'] = df['resale_price'].apply(categorize_price)


    # Create region categorization based on town - generate region column
    def get_region(town):
        central_towns = ['BISHAN', 'BUKIT MERAH', 'BUKIT TIMAH', 'CENTRAL AREA', 'GEYLANG',
                        'KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'TOA PAYOH']
        east_towns = ['BEDOK', 'PASIR RIS', 'TAMPINES']
        west_towns = ['BUKIT BATOK', 'BUKIT PANJANG', 'CHOA CHU KANG', 'CLEMENTI', 
                    'JURONG EAST', 'JURONG WEST']
        north_towns = ['SEMBAWANG', 'YISHUN', 'WOODLANDS']
        northeast_towns = ['ANG MO KIO', 'HOUGANG', 'SENGKANG', 'SERANGOON', 'PUNGGOL']
        
        if town in central_towns:
            return 'Central'
        elif town in east_towns:
            return 'East'
        elif town in west_towns:
            return 'West'
        elif town in north_towns:
            return 'North'
        elif town in northeast_towns:
            return 'North-East'
        else:
            return 'Other'

    df['region'] = df['town'].apply(get_region)

    # remove row with missing values
    df =df.dropna()

    # remove duplicates
    df = df.drop_duplicates()

    # Save the main transformed dataframe
    file_path_store = project_root / "data" / "processed" / "resale_flat_prices_2017_onwards_clean.csv"
    df.to_csv(file_path_store, index=False)
    print("Saved: resale_flat_prices_2017_onwards_clean.csv")

    print("\nTransformation complete!")

    return file_path_store