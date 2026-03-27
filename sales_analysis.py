import numpy as np
import pandas as pd
df=pd.read_csv("sales_data.csv")
print(df)

#First 5 rows
print(df.head())

#Last 5 rows
print(df.tail())

#Shapes
print("Shape: ",df.shape)

#Column Names
print("Columns: ",df.columns)

#Data Types
print("Data Type: ",df.dtypes)

#Missing Values
print(df.isna().sum())

print(df.duplicated().sum)

Revenue=df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
print(Revenue)

Total_revenue=df['Total_Sales'].sum()
print("Total Revenue: ₹",Total_revenue)

best_product = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(1)
print(best_product)

average_sales = df['Total_Sales'].mean()
print(average_sales)

#Total Quantity sold
total_quantity = df['Quantity'].sum()
print("Total Quantity Sold:", total_quantity)

#Highest Revenue Product
top_revenue_product = Revenue.head(1)
print(top_revenue_product)

#or

top_revenue_product=df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(1)
print("Top Revenue Product:", top_revenue_product)

#Lowest Revenue Product
Low_revenue_product=Revenue.tail(1)
print(Low_revenue_product)
#or

Low_revenue_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).tail(1)
print("Low Revenue Product:", Low_revenue_product)

print("\n SALES REPORT")
print("-"*30)

print(f"Total Revenue: ₹{Total_revenue}")
print(f"Best Selling Product: {best_product}")
print(f"Average Revenue per Sale: ₹{round(average_sales)}")

print("\n Insights:")
print("- Product with highest demand:", best_product)
print("- Total business revenue generated:", Total_revenue)
print("- Average transaction value:", round(average_sales))