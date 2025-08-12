import pandas as pd
import random
#df = pd.read_csv("covid_19_clean_complete.csv")
df = pd.read_csv("big_mart_sales.csv")
#print(df.head())
#print(df.index)
print(df.columns)
#index_list = [random.randint(1,49069) for i in range(49068)]
#df.index=index_list
#print(df.head(10))
#updated_data= df.set_index('Date', drop=True, inplace=True)
#print(updated_data)
#df.reset_index(drop=True, inplace=True)
#print(df.columns)
print(df.head(5))
#deaths_in_continents = df[df['WHO Region'] == 'Americas']
#print(deaths_in_continents.head(10))
#world_deaths= df.groupby('Deaths').sum()
#print(world_deaths)
#print(df[-10:])
#print(df.iloc[[1,2,3,4,5],[1,2,3,4,5]])
#df.set_index('Province/State', inplace=True)
#print(df.loc[['New South Wales','Victoria'], ['Date', 'Deaths']])
###sample_df = pd.DataFrame({
#"name": ["John", "Anna", "Peter"],
#"age": [28, 24, 35],
#"city": ["New York", "Paris", "Berlin"],
#"id": ['A012', 'A013','A014']
#})
#print(sample_df)
#print(sample_df.loc[1:2])
#print(sample_df.iloc[1:2])
#sample_df.set_index('id', inplace=True)
#print(sample_df)
#print(sample_df.loc['A012':'A014'])
#print(sample_df.iloc[1:2])
#
#print(df[(df['Province/State'] == 'New South Wales') |(df['Country/Region'] == 'Australia')])
#print(df['Province/State'].isin(['New South Wales', 'Victoria', 'Queensland', 'Western Australia', 'South Australia', 'Tasmania']))
#print(df.dtypes)
#print(df.select_dtypes('int64'))
## MODIFYING DATA
#print(df.isna().sum())

#printing unknown values
#df['Province/State'] = df['Province/State'].fillna('unknown')
#print(df['Province/State'])
#print(df.isna().sum())
#printing most frequent one
#most_frequent = df['Province/State'].mode()[0]
#df['Province/State'] = df['Province/State'].fillna(most_frequent)
#print(df['Province/State'])
#print(df.isna().sum())
#most_frequent = df['Province/State'].mode()[0]
# filling with forward and backward values
#df['Province/State'] = df['Province/State'].fillna(method ='ffill')
#df['Province/State'] = df['Province/State'].fillna(method ='bfill')
#print(df['Province/State'])
#print(df.isna().sum())
#print(df[(df['Province/State'].isna() == True)  , 'Province/State'])
#print(df['Province/State'].mode())
#WORKING ON  BIG MART SALES DATASET
#print(df['Item_Fat_Content'].value_counts())
#Mapping =  {
# 'Low Fat': 'LF',
#'Regular': 'R',
#'low fat': 'LF',
#'LF': 'LF',
#'reg' : 'R'

#}
#df['Item_Fat_Content'] = df['Item_Fat_Content'].map(Mapping)
#print(df['Item_Fat_Content'].value_counts())

#df['MRP_IN_USd'] = df.Item_MRP.apply(lambda x : x/84)
#print(df.head(5))
#print(df.columns)
#df = pd.get_dummies(df)
