
import pandas as pd

# Read data from CSV file
df = pd.read_csv("sample_boston_data.csv")
print("\nCSV Data:\n", df)

# Read data from Excel file
df1 = pd.read_excel("sample_boston_data.xlsx")
print("\nExcel Data:\n", df1)

# Read data from JSON file
df2 = pd.read_json("sample_boston_data.json")
print("\nJSON Data:\n", df2)


