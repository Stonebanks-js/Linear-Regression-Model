#IMPORTING THE LIBRARIES 

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 

#IMPORTING THE DATA.CSV FILE FROM FILES ON THE COMPUTER

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

#SPLITTING THE TEST SET AND TRAINING SET
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size = 1/3, random_state = 0)

#TRAINING THE SIMPLE LINEAR REGRESSION MODEL ON THE TRAINING SET

from sklearn.linear_model import LinearRegression
regressor =LinearRegression()   #creating an object of the linear regression class from scikit
regressor.fit (X_train, y_train )    #fitting our model on
print("Training complete.")
#PREDICTING VALUES FOR NEW DATAS USING OUR PRE-BUILT MODELS

#PREDICTING THE TEST SET RESULTS
predicted_salary = regressor.predict([[6.5]])     #[[6.5]]

#VISUALISING THE TRAINING SET RESULTS
plt.scatter(X_train, y_train, color = 'red') 
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#VISUALISING THE TEST SET RESULTS 
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

         

