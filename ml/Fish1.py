import ssl
import pandas as pd
ssl._create_default_https_context = ssl._create_unverified_context
fish = pd.read_csv('https://bit.ly/fish_csv_data')
# print(fish.head())
# print(pd.unique(fish['Species']))
fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
fish_target = fish['Species'].to_numpy()
# print(fish_input[:5])

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(fish_input,
                                            fish_target, random_state=42)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier(n_neighbors=3)
kn.fit(train_scaled, train_target)
# print(kn.score(train_scaled, train_target))
# print(kn.score(test_scaled, test_target))
# print(kn.classes_)

import numpy as np
proba = kn.predict_proba(test_scaled[:5])
# print(np.round(proba, decimals=4))

distances, indexes = kn.kneighbors(test_scaled[3:4])
print(train_target[indexes])
