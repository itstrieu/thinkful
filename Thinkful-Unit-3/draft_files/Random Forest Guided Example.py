import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
%matplotlib inline

y2015 = pd.read_csv(
    'Thinkful-Unit-3\LoanStats3d.csv',
    skipinitialspace=True,
    header=1
)

means = y2015[['loan_amnt','funded_amnt','funded_amnt_inv', 'installment']].mean(axis=0)
stds = y2015[['loan_amnt','funded_amnt','funded_amnt_inv', 'installment']].std(axis=0)
y2015['amount'] = (((y2015[['loan_amnt','funded_amnt','funded_amnt_inv', 'installment']] - means) / stds).mean(axis=1))

y2015 = y2015.drop(['loan_amnt', 'funded_amnt','member_id', 'url',
                    'installment', 'funded_amnt_inv', 'total_pymnt',
                    'settlement_amount', 'annual_inc_joint',
                    'hardship_payoff_balance_amount', 'open_acc', 'tax_liens', 'hardship_amount',
                    'orig_projected_additional_accrued_interest', 'total_rec_int', 'dti_joint'], 1)

y2015.corr()

from sklearn import ensemble
from sklearn.model_selection import cross_val_score

rfc = ensemble.RandomForestClassifier()

y2015 = y2015[:-2]

X = y2015.drop('loan_status', 1)
X = X.dropna(axis=1)
Y = y2015['loan_status']
Y = Y.fillna('')
X = pd.get_dummies(X)
cross_val_score(rfc, X, Y, cv=10)

sklearn_pca = PCA(n_components=4)
Y_sklearn = sklearn_pca.fit_transform(X)

cross_val_score(rfc, X, Y, cv=10)
