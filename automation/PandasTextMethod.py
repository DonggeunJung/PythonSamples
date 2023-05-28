import pandas as pd

info = pd.read_excel('./docs/employees.xlsx', sheet_name='Sheet1')
# print(info)
# info['Name'] = info['First name'] + info['Last name']
# info['Name1'] = info[['First name', 'Last name']].sum(1) # merge by column direction
# print(info[['First name', 'Last name', 'Phone', 'Name', 'Name1']])
# info['Code front'] = info['Code'].str[0:4] # front 4 digits of Code
# info['Phone end'] = info['Phone'].str[9:] # last 4 digits of phone
# print(info[['First name', 'Last name', 'Phone', 'Code front', 'Phone end']])
# info['County'] = info['Address'].str.split(' ').str[0]
# print(info[['First name', 'Last name', 'Phone', 'County']])
# info['Capital'] = info['Eng name'].str.upper()
# info['Pascal'] = info['Eng name'].str.capitalize()
# print(info[['First name', 'Last name', 'Eng name', 'Capital', 'Pascal']])
# info['Phone1'] = info['Phone'].str.replace('-', '', 1)
# info['Phone2'] = info['Phone'].str.replace('-', '',)
# print(info[['First name', 'Last name', 'Phone', 'Phone1', 'Phone2']])
info['Address len'] = info['Address'].str.len()
print(info[['First name', 'Last name', 'Address', 'Address len']])
