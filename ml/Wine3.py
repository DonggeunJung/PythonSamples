import ssl
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

# cross validation of RandomForest
from sklearn.model_selection import cross_validate
# from sklearn.ensemble import RandomForestClassifier
# rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)
# from sklearn.ensemble import ExtraTreesClassifier
# et = ExtraTreesClassifier(n_jobs=-1, random_state=42)

# from sklearn.ensemble import GradientBoostingClassifier
# gb = GradientBoostingClassifier(random_state=42)
# scores = cross_validate(gb, train_input, train_target,
#                         return_train_score=True, n_jobs=-1)
import numpy as np
# print(np.mean(scores['train_score']), np.mean(scores['test_score']))
# importances of 'alcohol', 'sugar', 'pH'
# gb.fit(train_input, train_target)
# print(gb.feature_importances_)
# print(et.oob_score_)

# from sklearn.ensemble import HistGradientBoostingClassifier
# hgb = HistGradientBoostingClassifier(random_state=42)
# scores = cross_validate(hgb, train_input, train_target,
#                         return_train_score=True)
# print(np.mean(scores['train_score']), np.mean(scores['test_score']))
# from sklearn.inspection import permutation_importance
# hgb.fit(train_input, train_target)
# result = permutation_importance(hgb, train_input, train_target,
#                                 n_repeats=10, random_state=42, n_jobs=-1)
# print(result.importances_mean)
# print(hgb.score(test_input, test_target))

from xgboost import XGBClassifier
xgb = XGBClassifier(tree_method='hist', random_state=42)
scores = cross_validate(xgb, train_input, train_target,
                        return_train_score=True)
print(np.mean(scores['train_score']), np.mean(scores['test_score']))

# from lightgbm import LGBMClassifier
# lgb = LGBMClassifier(random_state=42)
# scores = cross_validate(lgb, train_input, train_target,
#                         return_train_score=True, n_jobs=-1)
# print(np.mean(scores['train_score']), np.mean(scores['test_score']))
