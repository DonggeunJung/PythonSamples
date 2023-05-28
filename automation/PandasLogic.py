import pandas as pd
# from datetime import datetime

fruit = pd.read_excel('./docs/fruit_order.xlsx', sheet_name='Sheet1')
# fruit['Level'] = ''
# for idx, x in enumerate(fruit['Cost']) :
#     if x >= 500000 :
#         fruit['Level'].loc[idx] = 'over 500k'
#     elif x >= 200000 :
#         fruit['Level'].loc[idx] = 'over 200k'
#     else :
#         fruit['Level'].loc[idx] = 'less 200k'
pd.to_datetime(fruit['Date'])
pd.to_datetime(fruit['ExpiryDate'])
fruit['DayOfDate'] = fruit['Date'].dt.day
fruit['Today'] = pd.to_datetime('today').now()
fruit['OverDays'] = (fruit['Today'] - fruit['ExpiryDate']).dt.days
print(fruit[['Product', 'ExpiryDate', 'DayOfDate', 'Today', 'OverDays']].head())
