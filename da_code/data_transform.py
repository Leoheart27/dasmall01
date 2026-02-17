import ast
import pandas as pd
import json
import numpy as np

df = pd.read_csv("data_raw/products_cleaned2.csv")

df_rate = pd.DataFrame(df["rating"].apply(ast.literal_eval).tolist())

# change columns name
print(df_rate.columns)
df_rate.columns = ["rate", "rate count"]

# Concatenate the original DataFrame with the new DataFrame

df_final = pd.concat([df.drop(columns=["rating"]), df_rate], axis=1)
df_final = df_final.set_index("id")

print(df_final.head())
print(1)
# df_final.to_csv("data_raw/products_final2.csv", index=True)