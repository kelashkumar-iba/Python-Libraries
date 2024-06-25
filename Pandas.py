import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Love', 'Haresh', 'Kelash', 'Zeeshan'],
        'Age': [20, 18, 21, 23],
        'City': ['Naukot', 'Mithi', 'Sukkur', 'Karachi']}
df = pd.DataFrame(data)

print(df)

# Read the CSV file into a DataFrame
df = pd.read_csv("C:\\Users\Kelash Kumar\\Downloads\\temperatures.csv")

# Display the first few rows of the DataFrame
print(df.head())

# Display the last few rows of the DataFrame
print(df.tail())

# Display basic information about the DataFrame
print(df.info())

# Display summary statistics of numerical columns
print(df.describe())
