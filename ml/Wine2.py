import ssl

import numpy as np

ssl._create_default_https_context = ssl._create_unverified_context
import pandas as pd
# load wine data
wine = pd.read_csv('https://bit.ly/wine_csv_data')

# set "class" column as target, and other columns as input data
input = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()

# divide data with train set & test set
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(input,
                                    target, test_size=0.2, random_state=42)

# divide data with train-2 set & validation set
# sub_input, val_input, sub_target, val_target = train_test_split(
#     train_input, train_target, test_size=0.2, random_state=42)
# print(sub_input.shape, val_input.shape)

# train data by DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
# dt.fit(sub_input, sub_target)
# print(dt.score(sub_input, sub_target))
# print(dt.score(val_input, val_target))

# from sklearn.model_selection import cross_validate
# from sklearn.model_selection import StratifiedKFold
# splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
# scores = cross_validate(dt, train_input, train_target, cv=splitter)
# print(scores['test_score']) # list of each validation score
# import numpy as np
# print(np.mean(scores['test_score']))

from scipy.stats import uniform, randint
params = {'min_impurity_decrease' : uniform(0.0001, 0.001),
          'max_depth' : randint(20, 50),
          'min_samples_split' : randint(2, 25),
          'min_samples_leaf' : randint(1, 25)}
# from sklearn.model_selection import GridSearchCV
# gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
from sklearn.model_selection import RandomizedSearchCV
gs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42), params,
                        n_iter=100, n_jobs=-1, random_state=42)
gs.fit(train_input, train_target)
print(np.max(gs.cv_results_['mean_test_score'])) # score of each parameter
print(gs.best_params_) # a parameter for best score
dt = gs.best_estimator_
print(dt.score(train_input, train_target))
print(dt.score(test_input, test_target))
