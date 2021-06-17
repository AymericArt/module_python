import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_predictions.csv", index_col=0, parse_dates=True)
df.head(50)

# data = house_pricing.where(house_pricing['LotArea'] < 20000) and house_pricing.where(house_pricing['SalePrice'] < 50000)

# sales_predictions['date'] = pd.to_datetime(sales_predictions['date'])
df['date'] = pd.to_datetime(df['date'], format="%m/%d/%Y, %H:%M:%S")
sb.scatterplot(data=df, x="date", y="item_price")
