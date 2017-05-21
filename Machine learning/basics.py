from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets


data = datasets.load_iris()
features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names

for t in range(3):
    if t == 0:
        c = 'r'
        marker = '>'
    elif t == 1:
        c = 'g'
        marker = 'o'
    elif t == 2:
        c = 'b'
        marker = 'x'
    plt.scatter(features[target == t, 0], features[target == t, 0], marker=marker, c=c)
    plt.show()