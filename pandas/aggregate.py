import pandas as pd

df = pd.read_csv("dim_hotels.csv")

print(df.sum(numeric_only=True)) # sum of all numeric columns

# find mean of property_id column
mean_property_id = df["property_id"].mean()
print("Mean of property_id:", mean_property_id)

# find sum of property_id column
sum_property_id = df["property_id"].sum()
print("Sum of property_id:", sum_property_id)
# find maximum of property_id column
max_property_id = df["property_id"].max()
print("Maximum of property_id:", max_property_id)
# find minimum of property_id column
min_property_id = df["property_id"].min()
print("Minimum of property_id:", min_property_id)
# find count of property_id column
count_property_id = df["property_id"].count()
print("Count of property_id:", count_property_id)