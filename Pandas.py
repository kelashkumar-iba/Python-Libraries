import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Love', 'Haresh', 'Kelash', 'Zeeshan'],
        'Age': [20, 18, 21, 23],
        'City': ['Naukot', 'Mithi', 'Sukkur', 'Karachi']}
df = pd.DataFrame(data)

print(df)
