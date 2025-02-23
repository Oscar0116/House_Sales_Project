import pandas as pd

# Load the raw data
raw_data_path = r'C:\Users\oscar\OneDrive\Escritorio\Python_Projects\House_Sales_Project\data\kc_house_data_raw.csv'
df = pd.read_csv(raw_data_path)

# Display the first few rows to inspect the data
print("Raw Data Loaded for Cleaning:")
print(df.head())

# Remove unnecessary columns
df.drop(['id', 'Unnamed: 0'], axis=1, inplace=True)

# Handle missing values: Only fill missing values in numeric columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Check for any remaining issues with the date or categorical columns
# For date columns, ensure they are correctly formatted, if any
# If there are any non-numeric columns that should be treated as strings or categories, handle them here

# Save the cleaned data
cleaned_data_path = r'C:\Users\oscar\OneDrive\Escritorio\Python_Projects\House_Sales_Project\data\kc_house_data_cleaned.csv'
df.to_csv(cleaned_data_path, index=False)

print(f"Data cleaned and saved to: {cleaned_data_path}")


