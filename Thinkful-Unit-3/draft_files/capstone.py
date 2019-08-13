import json
import os
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score


# Begin data exploration
os.chdir("/Users/Mango/Documents/GitHub/Thinkful/Thinkful-Unit-3/nyt")

# Each dataset contains either articles or article comments per year. They need to be concatenated.
# First, I'll combine all articles into one dataset, and comments into another, with a column for the year the article was published.


df = pd.read_csv('ArticlesApril2017.csv')
df2 = pd.read_csv('CommentsApril2017.csv')

import re

REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

def preprocess_comments(commentBody):
    commentBody = [REPLACE_NO_SPACE.sub("", line.lower()) for line in commentBody]
    commentBody = [REPLACE_WITH_SPACE.sub(" ", line) for line in commentBody]

    return commentBody

df2.commentBody = preprocess_comments(df2.commentBody)

commentBody = df2.commentBody
