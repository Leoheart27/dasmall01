import pandas as pd
import numpy as np

df = pd.read_csv("data_raw/products_final.csv", index_col=0)

# sum of price per category sold
revenue_category = df.groupby("category")["price"].sum()
print("total revenue:")
print(" ")
print(revenue_category)
print("-------------------------------------------------")
# avarage rate per category
average_rate_category = df.groupby("category")["rate"].mean().round(2)
print("average rating per category")
print(" ")
print(average_rate_category)
print("-------------------------------------------------")
# total of rating per category
potentital_sold = df.groupby("category")["rate count"].sum()
print("potential sold by total rating")
print(" ")
print(potentital_sold)
print("-------------------------------------------------")

# total profit 
profit_category = df["price"].sum().round(2)
print("total profit")
print(" ")
print(profit_category)
