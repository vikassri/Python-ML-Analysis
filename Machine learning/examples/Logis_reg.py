from sklearn import datasets
from sklearn import metrics
from sklearn import linear_model

# loading dataset
dataset = datasets.load_iris()

# creating the model
model = linear_model.LogisticRegression()

# fitting the model on dataset
model.fit(dataset.data, dataset.target)

# check the model
print(model)

# expected values
expected = dataset.target

# preditcted the value using model
predicted = model.predict(dataset.data)

# printed the classification of report
print(metrics.classification_report(expected, predicted))

# printed the confusion matrix
print(metrics.confusion_matrix(expected, predicted))

# printing the accuracy score
print("\nAccuracy Score: {}".format(metrics.accuracy_score(expected, predicted)))

