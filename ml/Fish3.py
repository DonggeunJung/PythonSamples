import pandas as pd
fish = pd.read_csv('./docs/fish.csv')
fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
fish_target = fish['Species'].to_numpy()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(fish_input,
                                            fish_target, random_state=42)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=20, max_iter=1000)
lr.fit(train_scaled, train_target)
# print(lr.score(train_scaled, train_target))
# print(lr.score(test_scaled, test_target))
# print(lr.predict(test_scaled[:5]))
import numpy as np
proba = lr.predict_proba(test_scaled[:5])
# print(lr.classes_)
# print(np.round(proba, decimals=3))
print(lr.coef_.shape, lr.intercept_.shape)
