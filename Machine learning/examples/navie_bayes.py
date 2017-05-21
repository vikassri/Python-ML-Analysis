from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

# load the datasets
dataset = datasets.load_iris()

# creating the model
model = GaussianNB()
print(model)

# trying to fit the model
model.fit(dataset.data, dataset.target)

expected = dataset.target
predicted = model.predict(dataset.data)

# print the classification report
print(metrics.classification_report(expected, predicted))

# print the confusion metrics
print(metrics.confusion_matrix(expected, predicted))

# print the accuracy score
print("Accuracy Score: {}".format(metrics.accuracy_score(expected, predicted)))