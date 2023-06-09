import ssl
import pandas as pd
ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv('https://bit.ly/perch_csv_data')
perch_full = df.to_numpy()
# print(perch_full)

import numpy as np

perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(perch_full,
                                                perch_weight, random_state=42)

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=5, include_bias=False)
# sample = [[2, 3]]
# poly.fit(sample)
# print(poly.transform(sample))
poly.fit(train_input)
train_poly = poly.transform(train_input)
# print(train_poly.shape)
# print(poly.get_feature_names_out())
test_poly = poly.transform(test_input)

# from sklearn.linear_model import LinearRegression
# lr = LinearRegression()
# lr.fit(train_poly, train_target)
# print(lr.score(train_poly, train_target))
# print(lr.score(test_poly, test_target))

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

from sklearn.linear_model import Ridge
# train_score = []
# test_score = []
# alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
# for a in alpha_list :
#     ridge = Ridge(alpha=a)
#     ridge.fit(train_scaled, train_target)
#     train_score.append(ridge.score(train_scaled, train_target))
#     test_score.append(ridge.score(test_scaled, test_target))

import matplotlib.pyplot as plt
# plt.plot(np.log10(alpha_list), train_score)
# plt.plot(np.log10(alpha_list), test_score)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()
# ridge = Ridge(alpha=0.1)
# ridge.fit(train_scaled, train_target)
# print(ridge.score(train_scaled, train_target))
# print(ridge.score(test_scaled, test_target))

from sklearn.linear_model import Lasso
# train_score = []
# test_score = []
# alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
# for a in alpha_list :
#     lasso = Lasso(alpha=a, max_iter=10000)
#     lasso.fit(train_scaled, train_target)
#     train_score.append(lasso.score(train_scaled, train_target))
#     test_score.append(lasso.score(test_scaled, test_target))

# plt.plot(np.log10(alpha_list), train_score)
# plt.plot(np.log10(alpha_list), test_score)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

lasso = Lasso(alpha=10)
lasso.fit(train_scaled, train_target)
print(lasso.score(train_scaled, train_target))
print(lasso.score(test_scaled, test_target))
