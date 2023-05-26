import pandas as pd

score = pd.read_excel('./docs/scores.xlsx', sheet_name='Sheet1')
# print(score)
# total_kor = score['Kor'].sum(0) # sum by row direction
# print(total_kor)
# score['sum'] = score.iloc[:, 2:7].sum(1) # sum by column direction
# score['sum1'] = score['Kor'] + score['Eng'] + score['Math']\
#                 + score['Society'] + score['Science']
# avg_kor = score['Kor'].mean(0) # sum by row direction
# print(avg_kor)
# score['Avg'] = score.iloc[:, 2:7].mean(1) # average by row direction
# score['Avg1'] = (score['Kor'] + score['Eng'] + score['Math']\
#                  + score['Society'] + score['Science']) / 5
#print(score.head()) # upper 5 rows
# score1 = score.groupby(['Class']).sum()
# print(score1[['Kor', 'Eng', 'Math', 'Society', 'Science']])
# score['Rank'] = score['Avg'].rank(ascending=False)
# score['Rank_min'] = score['Avg'].rank(method='min', ascending=False)
# score_nums = score.iloc[:, [2,3,4,5,6]]
# score['Min'] = score_nums.min(1)
# score['Max'] = score_nums.max(1)
# print(score.head())
print(score.describe())
