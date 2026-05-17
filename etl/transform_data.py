import pandas as pd

#load cleaned datasets
orders=pd.read_csv("data/cleaned/orders_cleaned.csv")
payments=pd.read_csv("data/raw/olist_order_payments_dataset.csv")

# Merge datasets
merged_data=pd.merge(
orders,payments,on="order_id",how="left")

#create total payment metric
merged_data["total_payment"]=merged_data["payment_value"]

#convert purchase timestamp
merged_data["order_purchase_timestamp"]=pd.to_datetime(merged_data["order_purchase_timestamp"])

#extract business features
merged_data["purchase_year"]=merged_data["order_purchase_timestamp"].dt.year
merged_data["purchase_month"]=merged_data["order_purchase_timestamp"].dt.month

#save processed data
merged_data.to_csv("data/processed/olist_orders_transformed.csv",index=False)

print("Data transformation completed successfully.")
