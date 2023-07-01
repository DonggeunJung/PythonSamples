import numpy as np
import pandas as pd
fish = pd.read_csv('./docs/fish.csv')

# set "Species" column as target, and other columns as input data
fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
fish_target = fish['Species'].to_numpy()

# divide data with train set & test set
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(fish_input,
                                            fish_target, random_state=42)

# set standard using scikit-learn StandardScaler
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

# run Stochastic Gradient Descent 10 times
from sklearn.linear_model import SGDClassifier
sc = SGDClassifier(loss='log_loss', max_iter=100, tol=None, random_state=42)
sc.fit(train_scaled, train_target)

# one more epoch Stochastic Gradient Descent
# sc.partial_fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))

# sc = SGDClassifier(loss='log_loss', random_state=42)
# train_score = []
# test_score = []
# classes = np.unique(train_target)
#
# # train SGD 300 epoch
# for _ in range(0, 300):
#     sc.partial_fit(train_scaled, train_target, classes=classes)
#     train_score.append(sc.score(train_scaled, train_target))
#     test_score.append(sc.score(test_scaled, test_target))
#
# # graph of 300 epoch SGD
# import matplotlib.pyplot as plt
# plt.plot(train_score)
# plt.plot(test_score)
# plt.xlabel('epoch')
# plt.ylabel('accuracy')
# plt.show()
