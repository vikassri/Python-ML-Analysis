Task
You are given performance data of relationship managers (RMs) at a bank. Their performance is based on factors such as meeting targets, number of customers (who availed loans) acquired by them and the quality of their customers (customers who do not default are considered good while those who default are considered bad).

You are also given loan default data of customers served by the RMs.

Based on the given training data, you have to predict the performance of RMs given in the evaluation dataset.

Here are the datasets:

In the datasets, the first row contains the labels of the attributes. In the performance RM training data set, there is an additional final column (named overall_performance) which has the information on whether the RM is a low (0), medium (1) or high (2) performer.

1. loan_training_01.csv
2. loan_evaluation02.csv
3. rm_training_01.csv
4. rm_evaluation_02.csv

final output should be 
employee_id , overall_rating
1231, 2
4321, 1


Your task: Your task is to model the training datasets and predict the performance of RMs in the evaluation dataset as low (0), medium (1) or high (2) performers.

