"""
SELF-ASSESSMENT

1. A boolean filter selects only rows that meet a condition. For example,
   filtering region == "South" keeps South rows and removes all others.

2. df["revenue"] returns a Series (one column).
   df[["revenue"]] returns a DataFrame (still tabular).
   The distinction matters when methods require a DataFrame instead
   of a Series.

3. Pandas is faster and more scalable than Excel for analyzing large
   datasets because operations can be automated with code.
"""

import pandas as pd

# --------------------------------------------------
# Exercise 1
# --------------------------------------------------

df = pd.read_csv("data/retail_sales.csv")

print("\nEXERCISE 1")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# --------------------------------------------------
# Exercise 2
# --------------------------------------------------

south = df[df["region"] == "South"]

print("\nEXERCISE 2")
print(len(south))
print(south.head())

# --------------------------------------------------
# Exercise 3
# --------------------------------------------------

top5 = df.sort_values("revenue", ascending=False).head(5)

print("\nEXERCISE 3")
print(top5)

# --------------------------------------------------
# Exercise 4
# --------------------------------------------------

big_south = df[(df["region"] == "South") &
               (df["revenue"] > 1000)]

print("\nEXERCISE 4")
print(len(big_south))
print(big_south.head())

# --------------------------------------------------
# Exercise 5
# --------------------------------------------------

df["per_unit"] = df["revenue"] / df["quantity"]

print("\nEXERCISE 5")
print(df.head())
print("Mean per-unit price:")
print(df["per_unit"].mean())

# --------------------------------------------------
# Exercise 6
# --------------------------------------------------

print("\nEXERCISE 6")
print(df["region"].unique())
print(df["region"].value_counts())

# --------------------------------------------------
# Exercise 7
# --------------------------------------------------

subset = df[["region", "product", "revenue"]]

print("\nEXERCISE 7")
print(subset.shape)

# --------------------------------------------------
# Exercise 8
# --------------------------------------------------

df.to_csv("data/explored.csv", index=False)

print("\nEXERCISE 8")
print("Saved data/explored.csv")