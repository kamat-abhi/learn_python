import pandas as pd

# key data structure in pandas
# Series = one list
# DataFrame = full frame

df = pd.read_csv('sales_data_sample.csv', encoding='latin1') 
print(df.head(5))  # first 5 rows
print(df.tail(5))  # last 5 rows


print(df)

data = {
    "Name": ["John", "Jane", "Jim"],
    "Age": [28, 34, 29],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df1 = pd.DataFrame(data)
print(df1)

# df1.to_csv('output.csv', index=False)  # Save DataFrame to CSV
df1.to_excel('output.xlsx', index=False)  # Save DataFrame to Excel
df1.to_json('output.json', index=False)  # Save DataFrame to JSON