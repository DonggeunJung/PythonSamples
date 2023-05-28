import pandas as pd

product = pd.read_excel('./docs/ingradient_order.xlsx', sheet_name='product')
order = pd.read_excel('./docs/ingradient_order.xlsx', sheet_name='order')
# print(product.head())
product.set_index('Code', inplace=True) # set 'Code' column as index
order.set_index('Code', inplace=True) # set 'Code' column as index
order['Product'] = product['Product']
order['Price'] = product['Price']
order['OrderPrice'] = order['OrderCount'] * order['Price']
#print(order)
order.reset_index(inplace=True)
print(order.head())
