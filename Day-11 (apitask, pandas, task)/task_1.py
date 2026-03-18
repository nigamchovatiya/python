"""
here i analyse sales csv: find total
revenue per product and best selling
month.
"""

# --------------------------------------

import pandas as pd

# --------------------------------------
"""total revenue per product"""

df = pd.read_csv('vgsales.csv')
print(df)

# create revenue column
df["totalrevenue"] = df["priceperunit"] * df["unitsold"]

# total revenue per product
product_revenue = df.groupby('product')['totalrevenue'].sum()

print("\nTotal revenue per product:")
print(product_revenue)


# ---------------------------------------
"""best selling month"""

# convert date column to datetime object
df["date"] = pd.to_datetime(df["date"])

# add new month column in data
df["month"] = df["date"].dt.month

# calculate total monthly sales
monthly_sales = df.groupby('month')['totalrevenue'].sum()

print("\nMonthly revenue:")
print(monthly_sales)

# getting maximum sales month
best_sales_month = monthly_sales.idxmax()

print("\nBest selling month:", best_sales_month)



