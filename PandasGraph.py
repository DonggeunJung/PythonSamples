import pandas as pd
import matplotlib.pyplot as plt

graph = pd.read_excel('./docs/graph_data.xlsx', sheet_name='Sheet1')
# print(graph.head(6))
# graph.plot(y=['Kor', 'Eng'], grid = True, title = 'Line graph', color = ['green', 'red'])
# graph.plot.scatter(x = 'Class', y = 'Eng', color = 'red', title = 'English scatter')
# graph.iloc[:, 2:7].mean().plot.bar(grid = True, title = 'Subject average',\
#                                    color = 'orange', ylabel = 'Average')
# a = graph.iloc[:, 2:7].mean().plot.barh(grid = True, color = 'blue')
# a.set_xlabel('Average')
# a.set_title('Subject average')
# class_c = graph.groupby('Class').size()
# class_c.plot.pie(title = 'Class size', ylabel = 'Class', autopct = '%1.1f%%',\
#                  explode = (0.1, 0, 0), shadow = True) # margin 0.1 to 1st pie
# fruit = ['apple', 'grape', 'strawberry', 'mellon']
# sales = [12, 31, 24, 46]
# df = pd.Series(sales, index = fruit)
# df.plot.pie(title='Fruit sales', ylabel = 'fruit', autopct = '%1.1f%%',\
#             explode=(0.1, 0, 0, 0), shadow = True)
# a = graph['Eng'].plot.hist(bins = 20, color = 'lightblue', edgecolor = 'red',\
#         grid = True, title = 'Histogram') # max level count = 20
# a.set_xlabel('English score')
# a.set_ylabel('Frequent count')
# graph['Society'].plot.hist(bins = 20, color = 'blue', edgecolor = 'blue',\
#          alpha = 0.5, title = 'Histogram')
# graph['Science'].plot.hist(bins = 20, color = 'red', edgecolor = 'red',\
#          alpha = 0.5, grid = True)
graph.boxplot(column = ['Kor'], by = 'Class')
plt.show()
