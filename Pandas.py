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

# Display the shape of the DataFrame
print(df.shape)

# Select a single column
print(df['avg_temp_c'])

# Select multiple columns
print(df[['city', 'avg_temp_c']])

# Select rows by index
print(df.loc[0])  # First row
print(df.loc[1:5])  # First five rows

# Select rows and columns by label
print(df.loc[1:5, ['date', 'avg_temp_c']])

# Select rows and columns by position
print(df.iloc[0])  # First row
print(df.iloc[1:5, [0, 3]])  # First five rows, first and fourth columns

print([df.sort_values("avg_temp_c", ascending = False)])

# Filter rows where avg_temp_c is greater than 28
filtered_df = df[df['avg_temp_c'] > 37.5]
print(filtered_df)


# Group by city and compute the mean of avg_temp_c
grouped_df = df.groupby('city')['avg_temp_c'].mean()
print(grouped_df)

# Group by country and compute the sum of avg_temp_c
grouped_df = df.groupby('country')['avg_temp_c'].sum()
print(grouped_df)

print(df[(df['country'] == 'Pakistan') & (df['avg_temp_c'] > 34)])

