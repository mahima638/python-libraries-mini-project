import pandas as pd
import matplotlib.pyplot  as plt

df = pd.read_csv('covid_19_clean_complete.csv')
print(df.head())
print(df.columns)
#countries = df['Country/Region']
#print(countries)
#plt.bar(df['Date'], df['Deaths'] , color='red')
#plt.title('Death on respective dates')
#plt.xlabel('Date')
#plt.ylabel('Deaths')
#plt.show()
country_deaths = df.groupby('Country/Region')['Deaths'].sum()
top_10 = country_deaths.sort_values(ascending=False).head(10)
plt.figure(figsize=(10,8))
plt.pie(top_10, labels=top_10.index, autopct='%1.1f%%', startangle=90)
plt.title('Deaths in each country')
plt.show()