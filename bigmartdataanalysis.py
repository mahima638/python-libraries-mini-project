import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('big_mart_sales.csv')
print(df.head())
print(df.columns)
#print(df.tail())
#print(df['Item_Type'])
#print(df['Item_MRP'])
#print(df['Item_Outlet_Sales'])
#print(df['Outlet_Size'])
print(df.isnull().sum())
df['Item_Weight'].fillna(df['Item_Weight'].mean())
print(df.isnull().sum())
#print(df['Outlet_Size'])