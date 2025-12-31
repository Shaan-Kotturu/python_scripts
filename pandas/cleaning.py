import pandas as pd

df = pd.read_csv("dim_hotels.csv")

#drop a column
# df_dropped_column = df.drop(columns=["property_id"])

#drop a row that has missing values
# df_dropped_na = df.dropna(subset=["category"]) # drop rows where 'category' is NaN

#fill missing values in 'category' column with 'Unknown'
#df_filled_na = df.copy()
# df_filled_na["category"] = df_filled_na["category"].fillna("Unknown")

#replace "Bangalore" value in 'city' column with "Bengaluru"
df["city"] = df["city"].replace({"Bangalore" : "Bengaluru"})
print(df)
