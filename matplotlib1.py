# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned COVID-19 dataset
df = pd.read_csv('covid_19_clean_complete.csv')

# Display the first 5 rows of the dataset
print(df.head())

# Print all column names in the dataset
print(df.columns)

# === Pie Chart: Top 10 Countries by Total COVID-19 Deaths ===

# Group data by country and calculate the total deaths for each country
country_deaths = df.groupby('Country/Region')['Deaths'].sum()

# Sort the countries by total deaths in descending order and select the top 10
top_10 = country_deaths.sort_values(ascending=False).head(10)

# Set the size of the figure
plt.figure(figsize=(10, 8))

# Create a pie chart for the top 10 countries with highest deaths
plt.pie(top_10, labels=top_10.index, autopct='%1.1f%%', startangle=90)

# Set the title of the chart
plt.title('Top 10 Countries by Total COVID-19 Deaths')

# Display the plot
plt.show()
