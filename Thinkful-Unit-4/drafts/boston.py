import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import os
%matplotlib inline
from sklearn.datasets.samples_generator import make_blobs
from sklearn.model_selection import train_test_split

# Begin data exploration
os.chdir("/Users/Mango/Documents/GitHub/Thinkful/Thinkful-Unit-4/datasets")

df = pd.read_csv('results.csv')
df.describe()

df = df.drop(['state', 'name', 'city', 'ctz', 'bib'], axis=1)

#sns.distplot(df['age'])
#sns.distplot(df['pace'])

df.columns

features = ['division','5k', '10k', '20k', '25k', '30k', '35k', '40k',
       'genderdiv','overall', 'pace', 'official']

#features = df.drop(['bib', 'ctz', 'name', 'overall','state', 'country', 'city', 'gender'], axis=1)
df = df.replace('-', "")
df = df.replace(' ', '')

def to_float(column):
    df[column] = pd.to_numeric(df[column])

for x in features:
    df[x] = pd.to_numeric(df[x])

# Exploring different clusters: Gender, Age Group, Rank Group
def unique(list1):

    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    for x in unique_list:
        print (x)

unique(df['gender'])
unique(df['age'])

df = pd.get_dummies(df, columns=['age', 'gender'])
df.replace([np.inf, -np.inf], np.nan)
df=df.dropna()
# Preparing to cluster.

df.dtypes

X = df[features]
y = df.gender_F

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.9,
    random_state=42)

df.loc[:, df.isnull().any()]

from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from sklearn.cluster import MiniBatchKMeans


from sklearn.cluster import MeanShift, estimate_bandwidth

# Here we set the bandwidth. This function automatically derives a bandwidth
# number based on an inspection of the distances among points in the data.
bandwidth = estimate_bandwidth(X_train, quantile=0.2, n_samples=500)

# Declare and fit the model.
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X_train)

# Extract cluster assignments for each data point.
labels = ms.labels_

# Coordinates of the cluster centers.
cluster_centers = ms.cluster_centers_

# Count our clusters.
n_clusters_ = len(np.unique(labels))

print("Number of estimated clusters: {}".format(n_clusters_))

plt.scatter(X_train[:, 0], X_train[:, 1], c=labels)
plt.show()

print('Comparing the assigned categories to the ones in the data:')
print(pd.crosstab(y_train,labels))

from sklearn.cluster import SpectralClustering

from sklearn.cluster import AffinityPropagation
from sklearn import metrics
