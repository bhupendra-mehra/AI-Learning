import pandas as ps

df = ps.read_csv("sales.csv")

# print(df.sort_values("Price", ascending=True))

# print(df.sort_values("Quantity"))

# Sort by category, then highest price within each category
# print(
#     df.sort_values(
#         ["Category", "Price"],
#         ascending=[True, False],
#     )
# )

#To get the three most expensive orders:
top_3 = df.sort_values("Price", ascending=False).head(3)
print(top_3[["OrderID", "Product", "Price"]])