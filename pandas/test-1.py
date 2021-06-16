import pandas as pd
import numpy as np

house_pricing = pd.read_csv("data/house_pricing.csv", index_col=0, parse_dates=True)
# print(house_pricing.head())
# print(pd.Series(house_pricing))

s1 = pd.Series([1, 2, 3], ['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], ['a', 'd', 'c'])
plus = s1 + s2
moins = s1 - s2
fois = s1 * s2
div = s1 / s2;

ar = np.array([[1.1, 2, 3.3, 4], [2.7, 10, 5.4, 7], [5.3, 9, 1.5, 15]])
df = pd.DataFrame(ar, index = ['a1', 'a2', 'a3'], columns = ['A', 'B', 'C', 'D'])


dico = {'A': [1.1, 2.7, 5.3],
        'B': [2, 10, 2],
        'C': [3.3, 5.4, 1.5],
        'D': [4, 7, 15]}
df = pd.DataFrame(dico, index = ['a1', 'a2', 'a3']);

print(df.loc['a1'])