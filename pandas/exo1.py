import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt


house_pricing = pd.read_csv("data/house_pricing.csv", index_col=0, parse_dates=True)
house_pricing.head(10)
types = house_pricing.dtypes
print(pd.Series(types))
print(house_pricing.describe(include='all'))
print(pd.Series(house_pricing.isnull().sum()).sort_values(ascending=False))

data = house_pricing.where(house_pricing['LotArea'] < 20000) and house_pricing.where(house_pricing['SalePrice'] < 50000)


sb.scatterplot(data=data, x="SalePrice", y="LotArea")
