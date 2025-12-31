import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],}
df = pd.DataFrame(data)
# print(df)
# print(df.loc[1])  # Accessing the second row by label
#add a new column

df["City"] = ["New York", "Los Angeles", "Chicago"]
# print(df)

# add a new row
new_row = pd.DataFrame([{"Name": "David", "Age": 28, "City": "Miami"}])
df = pd.concat([df, new_row], ignore_index=True)
print(df)