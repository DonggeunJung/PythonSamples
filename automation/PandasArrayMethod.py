import pandas as pd

work = pd.read_excel('./docs/working_type.xlsx', sheet_name='Sheet1')
# print(work)
# w1 = work.loc[work['Department'] == 'production']
# w2 = work.loc[work['WorkingType'].isin(['register'])]
# print(w1, end='\n\n')
# w2 = work.loc[(work['Department'] == 'production') | (work['WorkingType'] =='register')]
# w2 = work.loc[~work['Department'].isin(['production'])]
# print(w2)
# w1 = work.sort_values(by = 'Code')
# w1 = work.sort_index()
# print(w1.head())
# print(work.duplicated())
print(work.drop_duplicates())
