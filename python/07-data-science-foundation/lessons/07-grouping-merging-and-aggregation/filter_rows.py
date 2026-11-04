import pandas as pd

df = pd.read_csv("sales.csv")

## start filter rows with single column 
# Orders where the price is greater than 1,000
print(df[df["Price"] > 1000])

# Only completed orders
print(df[df["Status"] == "Completed"])

# Orders with quantity greater than or equal to 2
print(df[df["Quantity"] >= 2])

## end filter

##start filter with multilple column filters

result = df[
    (df["Price"] > 1000) &
    (df["Status"] == "Completed")
]

print(result)

result = df[df["Product"].isin(["Monitor","Laptop"])]

print(result)
##end