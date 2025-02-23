import pandas as pd

# Define the URL for the raw data
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'

# Load the data directly from the URL
df = pd.read_csv(url)

# Display the first few rows to verify it's loaded correctly
print("Data loaded successfully!")
print(df.head())

# Save the raw data to the 'data' folder
raw_data_path = r'C:\Users\oscar\OneDrive\Escritorio\Python_Projects\House_Sales_Project\data\kc_house_data_raw.csv'
df.to_csv(raw_data_path, index=False)

print(f"Raw data saved to: {raw_data_path}")

import pandas as pd

# Load the cleaned dataset
file_path = 'C:/Users/oscar/OneDrive/Escritorio/Python_Projects/House_Sales_Project/data/kc_house_data_cleaned.csv'
df = pd.read_csv(file_path)

# Display the data types of each column
print(df.dtypes)
