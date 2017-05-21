from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

# loading the dataset
dataset = datasets.load_iris()

# defining the model
model = DecisionTreeClassifier()

# fitting the model
model.fit(dataset.data, dataset.target)

# expected value
expected = dataset.target

# predicting the model
predicted = model.predict(dataset.data)

# print the classification matrix
print(metrics.classification_report(expected, predicted))

# print the confusion matrix
print(metrics.confusion_matrix(expected, predicted))

# printing the Accuracy score
print("Accuracy Score : {}".format(metrics.accuracy_score(expected, predicted)))