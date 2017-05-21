from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# loading the dataset
dataset = datasets.load_iris()

# creating the model
model = KNeighborsClassifier()
print(model)

# fitting the model
model.fit(dataset.data, dataset.target)

expected = dataset.target
predict = model.predict(dataset.data)

# print the classification
print(metrics.classification_report(expected, predict))

# print the confusion metrics
print(metrics.confusion_matrix(expected, predict))

# print the accuracy score
print("Accuracy Score :{}".format(metrics.accuracy_score(expected, predict)))