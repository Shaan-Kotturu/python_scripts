import pandas as pd

df = pd.read_csv("dim_hotels.csv")
print(df)
# print(df.to_string())

#selecting a single column
# print(df["property_name"])
# print(df[["property_name", "city"]])

#selecting by row
# print(df.loc[0])  #first row
# print(df.loc[0:2])  #first three rows