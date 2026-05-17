import pandas as pd

# Load datasets
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

customers = pd.read_csv("data/raw/olist_customers_dataset.csv")

# Preview data
print(orders.head())

# Dataset information
print(orders.info())

# Missing values
print(orders.isnull().sum())