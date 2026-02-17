import pandas as pd

df = pd.read_csv("data_raw/products.csv")

df_clean = df.copy().set_index("id").drop(columns=["description", "image"], inplace=False)


df_clean.to_csv("data_raw/products_cleaned2.csv", index="id")
print(1)