# imports
from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# loading the dataset
iris = datasets.load_iris()

# iris data count
print("count of Instances: %i" % len(iris.data))
print("count of target: %i" % len(iris.target))
print("Attribute : {}, {}, {}, {}".format("Sepel length", "Sepel width", "petal length", "petal width"))

# taking sepel length/width
X, y = iris.data[:, :2], iris.target

# breaking the dataset into training and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=101)

# implementing the standard Scaler to convert them into standard deviation
scaler = preprocessing.StandardScaler().fit(X_train)

# transforming them into scalar
X_train = scaler.transform(X_train)

# transforming them into scalar
X_test = scaler.transform(X_test)

# now implement the knn model
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

# prediction of values
y_pred = knn.predict(X_test)

# score of prediction
print("Accuracy Score: %0.2f " % accuracy_score(y_test, y_pred))