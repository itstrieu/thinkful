import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
%matplotlib inline

# Loading data and features engineering
data = pd.read_csv('Thinkful-Unit-3/onp.csv')
data = data.rename(columns=lambda x: x.strip())

def share_fun(row):
    if row['shares'] > 1400:
        return 1
    if row['shares'] <= 1400:
        return 0

data['shares_binary'] = data.apply(lambda row: share_fun(row), axis=1)
data['shares_rate'] = data['shares']/data['timedelta']

data = data.drop(['url', 'n_non_stop_words', 'n_non_stop_unique_tokens',
                    'kw_max_max', 'kw_avg_max', 'kw_min_avg'], 1)



features=data.columns[7:54]
X = data[features]
X = pd.get_dummies(X)
Y = data['shares_binary']


# Holdout Groups
from sklearn.model_selection import train_test_split
# Use train_test_split to create the necessary training and test groups
X_train, X_test, Y_train, Y_test = train_test_split(data, Y, test_size=0.2, random_state=20)

# Logistic Regression
lr = LogisticRegression(C=.9)
fit = lr.fit(X, Y)

print('Coefficients')
print(fit.coef_)
print(fit.intercept_)
pred_y_sklearn = lr.predict(X)

print('\n Accuracy by admission status')
print(pd.crosstab(pred_y_sklearn, Y))

print('\n Percentage accuracy')
print(lr.score(X, Y))

# Ridge regression
ridgeregr = linear_model.Ridge(alpha=.5, fit_intercept=False)
ridgeregr.fit(X_train, Y_train)
print(ridgeregr.score(X_test, Y_test))

# LASSO Regression
lass = linear_model.Lasso(alpha=.1)
lassfit = lass.fit(X_train, Y_train)
print(lass.score(X_test, Y_test))

# Cross Validation Scores
print('vanilla cv score:\n', cross_val_score(lr, X_test, Y_test, cv=10))
print('lasso cv score:\n', cross_val_score(lass, X_test, Y_test, cv=10))
print('ridge cv score:\n', cross_val_score(ridgeregr, X_test, Y_test, cv=10))
