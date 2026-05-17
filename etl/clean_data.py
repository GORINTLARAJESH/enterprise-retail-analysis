import pandas as pd 

# Load datasets
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")

#check missing values
print("missing values:")
print(orders.isnull().sum())

#remove duplicates rows
orders=orders.drop_duplicates()

#convert date columns
date_columns=[
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]
for col in date_columns:
    orders[col]=pd.to_datetime(orders[col])

#check data types
print("\nData types:")
print(orders.dtypes)

#save cleaned data
orders.to_csv("data/cleaned/olist_orders_cleaned.csv", index=False)

print("\nData cleaning completed successfully.")
