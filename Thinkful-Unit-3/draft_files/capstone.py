import json
import os
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score


# Begin data exploration
os.chdir("/Users/Mango/Documents/GitHub/Thinkful/Thinkful-Unit-3/nyt")
df = pd.read_csv('ArticlesApril2017.csv')
df2 = pd.read_csv('CommentsApril2017.csv')


df2.articleID.unique
