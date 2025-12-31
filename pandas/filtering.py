import pandas as pd

df = pd.read_csv("dim_hotels.csv")
# Filtering rows where city is 'Mumbai'
mumbai_hotels = df[df["city"] == "Mumbai"]
print(mumbai_hotels)

# filtering rows where category is 'Luxury' and city is 'Delhi'
delhi_luxury_hotels = df[(df["category"] == "Luxury") & (df["city"] == "Delhi")]
print(delhi_luxury_hotels)