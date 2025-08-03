import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('big_mart_sales.csv')

# Display the first few rows and column names
print(df.head())
print(df.columns)

# ---------------------------------------------
# Basic Data Cleaning (commented for flexibility)
# ---------------------------------------------

# Handling missing values (options shown below; uncomment one of them based on your choice)

# Fill missing 'Item_Weight' and 'Outlet_Size' with their mean values
# df['Item_Weight'] = df['Item_Weight'].fillna(df['Item_Weight'].mean())
# df['Outlet_Size'] = df['Outlet_Size'].fillna(df['Outlet_Size'].mean())

# Or fill missing values using forward fill method
# df['Item_Weight'] = df['Item_Weight'].fillna(method='ffill')
# df['Outlet_Size'] = df['Outlet_Size'].fillna(method='ffill')

# Or fill missing values with a constant (e.g., 'unknown')
# df['Item_Weight'] = df['Item_Weight'].fillna('unknown')
# df['Outlet_Size'] = df['Outlet_Size'].fillna('unknown')

# ---------------------------------------------
# Data Visualization
# ---------------------------------------------

# Line plot: Relationship between Item MRP and Sales
sns.lineplot(x='Item_MRP', y='Item_Outlet_Sales', data=df, color='red')
plt.title('MRP vs Sales')
plt.savefig('mrp_vs_sales.png', dpi=300, bbox_inches='tight')
plt.show()

# Bar plot: Sales by different Item Types
sns.barplot(x='Item_Type', y='Item_Outlet_Sales', data=df)
plt.xticks(rotation=90)
plt.title('Sales by Item Type')
plt.savefig('item_vs_outletsales.png', dpi=300, bbox_inches='tight')
plt.show()

# Heatmap: Correlation matrix for all numeric columns
numeric_df = df.select_dtypes(include=['number'])  # selecting numeric columns
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('relational_corr.png', dpi=300, bbox_inches='tight')
plt.show()

# Bar plot: Distribution of Item Types (count, not sales)
sns.countplot(x='Item_Type', data=df, color='blue')
plt.xticks(rotation=90)
plt.title('Item Type Distribution')
plt.savefig('Item_bar.png', dpi=300, bbox_inches='tight')
plt.show()

# Pie chart: Distribution of Fat Content
fat_content = df['Item_Fat_Content'].value_counts()
plt.pie(fat_content, labels=fat_content.index, autopct='%1.1f%%')
plt.title('Fat Content Distribution')
plt.savefig('fat_content.png', dpi=300, bbox_inches='tight')
plt.show()
