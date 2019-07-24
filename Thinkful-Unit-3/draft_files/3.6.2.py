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

df = pd.read_csv('Thinkful/Thinkful-Unit-3/datasets/2008.csv')
df = df.drop(['Year'], 1)

def add_delay(row):
    return row['CarrierDelay'] + row['WeatherDelay'] + row['NASDelay'] + row['SecurityDelay'] + row['LateAircraftDelay']

df['total_delay'] = df.apply(lambda row: add_delay(row), axis=1)

df.fillna(value={'total_delay': 0})

features = ['Month', 'DayofMonth', 'DayOfWeek', 'DepTime', 'CRSDepTime',
       'ArrTime', 'CRSArrTime', 'UniqueCarrier',
       'ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay',
       'DepDelay', 'Distance', 'TaxiIn', 'TaxiOut',
       'Cancelled', 'Diverted']
X = df[features]
X = pd.get_dummies(X)
Y = df['total_delay']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=20)

lr = LogisticRegression(C=.9)
fit = lr.fit(X_train, Y_train)
print(lr.score(X_test, Y_test))
