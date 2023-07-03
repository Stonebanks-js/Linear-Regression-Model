Importing the necessary libraries:

numpy (as np): A library for numerical operations in Python.
matplotlib.pyplot (as plt): A library for creating visualizations in Python.
pandas (as pd): A library for data manipulation and analysis in Python.

-----------------------------------------------------------------------------------------------------------------------------------------------------


Importing the data from a CSV file:

The code assumes that there is a file named 'Salary_Data.csv' in the same directory as the script.
The data is read using the read_csv function from pandas, and the independent variable (X) and dependent variable (y) are extracted from the dataset.

-----------------------------------------------------------------------------------------------------------------------------------------------------

Splitting the data into training and test sets:

The train_test_split function from scikit-learn is used to split the data into training and test sets.
The test set size is set to one-third (test_size=1/3) of the entire dataset.
The random_state parameter ensures reproducibility of the split.

-----------------------------------------------------------------------------------------------------------------------------------------------------

Training the linear regression model:

The LinearRegression class from scikit-learn is used to create a regression object named regressor.
The fit method is called to train the model using the training data.

-----------------------------------------------------------------------------------------------------------------------------------------------------

Predicting values for new data:

A single prediction is made for the years of experience value 6.5 using the predict method of the regressor object.

-----------------------------------------------------------------------------------------------------------------------------------------------------

Visualizing the training set results:

A scatter plot is created using plt.scatter to show the actual training data points (years of experience vs. salary).
The regression line is plotted using plt.plot, with the years of experience from the training set on the x-axis and the predicted salaries on the y-axis.
Title, xlabel, and ylabel are set to label the plot, and plt.show() is called to display the plot.

-----------------------------------------------------------------------------------------------------------------------------------------------------

Visualizing the test set results:

Similar to the training set results, a scatter plot is created to show the actual test data points.
The regression line is plotted using the training set data, as the model is already trained on it.
Title, xlabel, and ylabel are set to label the plot, and plt.show() is called to display the plot.

-----------------------------------------------------------------------------------------------------------------------------------------------------
