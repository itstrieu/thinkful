
import json
import os
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from sklearn import ensemble
from sklearn.model_selection import cross_val_score

# Use one of the following datasets to perform sentiment
# analysis on the given Amazon reviews.
# The goal is to create a model to algorithmically
# predict if a review is positive or negative just based on its text.
# Try to see how these reviews compare across categories.
# Does a review classification model for one category work for another?

os.chdir("/Users/Mango/Documents/GitHub/Thinkful/Thinkful-Unit-3/datasets")

df = pd.read_json("Pet_Supplies_5.json", lines=True)
df.drop(['asin', 'reviewerID', 'reviewerName'], 1)

df.reviewText_lower = df.reviewText.str.lower() # lowercase all review text

words = ['waste', 'horrible', 'not worth', 'junk', 'cheap', 'does not work', 'low quality',
            'misleading', 'ugh', 'disappointing', "zero stars", 'wonderful', 'excellent', 'perfect', 'great', 'awesome', 'great', 'loved', 'love',
            'liked', 'like', 'enjoyed', 'really well', 'works well', 'enjoyable', 'high quality',
            'pretty cool', 'happy', 'entertaining', 'nice']

for word in words:
    df[str(word)] = df.reviewText.str.contains(
    ' ' + str(word) + ' '
    )

df.head()

# outcome

def review_score(row):
    if row['overall'] >= 3:
        return "1"
    return "0"

df['outcome_binary'] = df.apply(lambda row: review_score(row), axis=1)

# df.reviewText.apply(lambda x: pd.value_counts(x.split(" "))).sum(axis=0)

#from collections import Counter
#text_list = list(df['reviewText'])
#text_list = " ".join(text_list)
#counts = Counter(text_list).most_common(10)
#print(counts)

rfc = ensemble.RandomForestClassifier()
X = df[words]
Y = df['outcome_binary']

cross_val_score(rfc, X, Y, cv=10)

#cv_score = cross_val_score(rfc, X, Y, cv=10)
#cv_score.mean()

rfc.fit(X, Y)

feature_importance = rfc.feature_importances_
feature_importance = 100* (feature_importance/feature_importance.max())
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + .5
plt.subplot(1,2,2)
plt.barh(pos, X.columns[sorted_idx], align='center')
plt.yticks(pos, X.columns[sorted_idx])
plt.show()


#test = []
#for variable in df.summary:
#    for row in variable:
#        test.append(row.split())
