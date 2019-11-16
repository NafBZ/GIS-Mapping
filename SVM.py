import pandas as pd
import numpy as np
import sklearn
import matplotlib
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_validate

np.random.seed(123)

data = pd.read_csv("Risk Data.csv", sep = ",")
#print(data.head())

data = data[["POPULATION", "DISTANCE_FROM_SEA", "ALTITUDE", "ANNUAL_RAINFALL", "Risk"]]
#print(data.head())
target = "Risk"

x = np.array(data.drop([target], 1))
y = np.array(data[target])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.2, random_state= 123)

classes = ["High", "Medium", "Low"]

model = svm.SVC(kernel = "linear", C = 2)

model.fit(x_train, y_train)

prediction = model.predict(x_test)

acc = metrics.accuracy_score(y_test, prediction)

print(acc)

"""
for x in range(len(prediction)):
    print(prediction[x], x_test[x], y_test[x])
"""

cv_predict = cross_val_predict(model, x, y, cv = 10)
cv_score = cross_val_score(model, x, y, cv = 10)
avg_score = np.mean(cv_score)
print(cv_predict)
print(cv_score)
print(avg_score)

conf_matrix = metrics.confusion_matrix(y, cv_predict)
print(conf_matrix)
evaluation = metrics.classification_report(y, cv_predict)
print(evaluation)
metrics.confusion_matrix()





