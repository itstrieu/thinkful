import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn import tree
from IPython.display import Image
import pydotplus
import graphviz

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
Y = data['shares_binary']

decision_tree = tree.DecisionTreeClassifier(
    criterion='entropy',
    max_features=1,
    max_depth=4,
    random_state = 1337
)
decision_tree.fit(X, Y)

dot_data = tree.export_graphviz(
    decision_tree, out_file=None,
    feature_names=features,
    class_names=['Popular', 'Unpopular'],
    filled=True
)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())


from sklearn import ensemble
from sklearn.model_selection import cross_val_score

rfc = ensemble.RandomForestClassifier()
cross_val_score(rfc, X, Y, cv=10)
