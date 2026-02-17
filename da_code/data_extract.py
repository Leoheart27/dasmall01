import requests as req
import pandas as pd

url = "https://fakestoreapi.com/products"
response = req.get(url)

data = response.json()

df = pd.DataFrame(data)

df.to_csv("data_raw/products.csv", index=False)