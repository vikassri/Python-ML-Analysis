from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets
"""
If the goal is to separate the three types of  owers, we can immediately make a few suggestions
just by looking at the data. For example, petal length seems to be able to separate Iris Setosa
from the other two  ower species on its own. We can write a little bit of code to discover where the cut-off is:

"""

data = datasets.load_iris()
features = data.data
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
feature_names = data.feature_names
target = data.target

# ['setosa' 'versicolor' 'virginica']
target_names = data.target_names

# We use NumPy fancy indexing to get an array of strings:
labels = target_names[target]

# The petal length is the feature at position 2
plength = features[:, 2]

# Build an array of booleans:
is_setosa = (labels == 'setosa')

max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print('Maximum of setosa: {0}.'.format(max_setosa))

features = features[~is_setosa]
labels = labels[~is_setosa]
is_virginica = (labels == 'virginica')

# Initialize best_acc to impossibly low value
best_acc = -1.0

for fi in range(features.shape[1]):
    # We are going to test all possible thresholds
    thresh = features[:, fi]
    for t in thresh:
        # Get the vector for feature `fi`
        feature_i = features[:, fi]
        # apply threshold `t`
        pred = (feature_i > t)
        acc = (pred == is_virginica).mean()
        rev_acc = (pred == ~is_virginica).mean()
        if rev_acc > acc:
            reverse = True
            acc = rev_acc
        else:
            reverse = False
        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            best_t = t
            best_reverse = reverse


def is_virginica_test(fi, t, reverse, example):
    "Apply threshold model to a new example"
    test = example[fi] > t
    if reverse:
        test = not test
    return test