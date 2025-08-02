import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
sns.set()
sns.set(style='darkgrid')
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = (10,10)
height = [3, 12, 5, 18, 45]
weight = [2, 3, 4, 3, 2]
calories_burnt = [3, 4, 5, 6, 2]
print("Hello")
#plt.figure(figsize=(10,5))
#plt.plot(height, weight)

#plt.plot( calories_burnt, marker ='o', linestyle='--')
#plt.legend(labels=['height', 'calories_burnt'])
#plt.xticks(ticks=[0,1,2,3,4], labels =['m1', 'm2', 'm3', 'm4', 'm5'], rotation=45)
#plt.xlabel('Height')
#plt.ylabel('Weight')
#plt.show()
#ig ,ax = plt.subplots(nrows=2, ncols=2, figsize =(12,6), sharex=True, sharey=True)
#ax[0].plot(calories_burnt,'go')
#ax[1].plot(weight)
#ax[0].set_title('calories_burnt')
#ax[1].set_title('weight')
#ax[0].set_xticks(ticks=[0,1,2,3,4])
#ax[1].set_xticks(ticks=[0,1,2,3,4])
#ax[1].set_xticklabels(labels=['m1', 'm2', 'm3', 'm4', 'm5'], rotation=45)
#ax[0].set_xticklabels(labels=['m1', 'm2', 'm3', 'm4', 'm5'], rotation=45)
#Data visualization

df = pd.read_csv('big_mart_sales.csv')
#df = df.dropna(how='any')
#print(df.columns)
#price_by_item = df.groupby('Item_Type').Item_MRP.mean()[:10]
#print(price_by_item)
#x= price_by_item.index.tolist()
#y=price_by_item.values.tolist()
#plt.figure(figsize=(10,5))
#plt.title('Price by item')
#plt.xlabel('Item')
#plt.ylabel('Price')
#plt.xticks(labels=x , ticks = np.arange(len(x)))
#plt.plot(x,y, marker='o', linestyle='--')


# sales_by_outletsize = df.groupby('Outlet_Size').Item_Outlet_Sales.sum()
# sales_by_outletsize.sort_values(inplace=True)
# x= sales_by_outletsize.index.tolist()
# y=sales_by_outletsize.values.tolist()
# plt.figure(figsize=(10,5))
# plt.title('Sales by outlet size')
# plt.xlabel('Outlet size')
# plt.ylabel('Sales')
# plt.xticks(labels=x , ticks = np.arange(len(x)))
# plt.bar(x,y,color=['red','orange','blue'])

# plt.xlabel('Item MRP')
# plt.ylabel('Item outlet sales')
# plt.scatter(df['Item_MRP'][:100], df['Item_Outlet_Sales'][:100], s= df['Item_Visibility'][:100]*1000,c='red' )

#data visualization with seaborn
# sns.lineplot(x='Item_Weight', y='Item_MRP', data=df[:50])
# sns.barplot(x="Item_Type", y="Item_MRP", data=df[:5])
# sns.distplot(df["Item_MRP"])
# sns.boxplot(df['Item_Outlet_Sales'], orient='v')
# sns.relplot(x="Item_MRP", y="Item_Outlet_Sales",hue="Item_Type", data=df[:200])
##if you want to see the relation between a catogorical and a conitnuous variable you can use stripplot or swarmplot
sns.catplot(x="Outlet_Size", y="Item_Outlet_Sales", kind='strip', data=df[:250])
sns.catplot(x="Outlet_Size", y="Item_Outlet_Sales", kind='swarm', data=df[:250])
sns.catplot(x="Outlet_Size", y="Item_Outlet_Sales", kind='box', data=df)
sns.catplot(x="Outlet_Size", y="Item_Outlet_Sales", kind='violin', data=df)
sns.catplot(x="Outlet_Size", y="Item_Outlet_Sales", kind='boxen', data=df)


