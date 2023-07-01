import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd
# load wine data
wine = pd.read_csv('https://bit.ly/wine_csv_data')
# print(wine.head())
# print(wine.info())
# print(wine.describe())

# set "class" column as target, and other columns as input data
input = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()

# divide data with train set & test set
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(input,
                                    target, test_size=0.2, random_state=42)

# set standard using scikit-learn StandardScaler
# from sklearn.preprocessing import StandardScaler
# ss = StandardScaler()
# ss.fit(train_input)
# train_scaled = ss.transform(train_input)
# test_scaled = ss.transform(test_input)

# train data by LogisticRegression
# from sklearn.linear_model import LogisticRegression
# lr = LogisticRegression()
# lr.fit(train_scaled, train_target)
# print(lr.score(train_scaled, train_target))
# print(lr.score(test_scaled, test_target))

# train data by DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(train_input, train_target)
print(dt.score(train_input, train_target))
print(dt.score(test_input, test_target))

# draw tree node graph
# import matplotlib.pyplot as plt
# from sklearn.tree import plot_tree
# plt.figure(figsize=(10,7))
# plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
# plt.show()

print(dt.feature_importances_)
