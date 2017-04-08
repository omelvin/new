

import pandas as pd

file_transactions = 'C:\\transactions'
transactions = pd.read_csv(file_transactions, nrows=100000)

date_cols = ['item_created_at', 'item_ship_by_date', 'fulfillment_shipped_at', 'fulfillment_created_at']
for col in date_cols:
    transactions[col] = pd.to_datetime(transactions[col], errors='coerce')