#######################################################################
#
# Importing Required Libraries ->
#
# pandas is used to load and analyze the dataset.
# matplotlib.pyplot is used to create graphs.
# train_test_split divides the dataset into training and testing data.
# DecisionTreeClassifier creates the Decision Tree model.
# accuracy_score calculates the model accuracy.
# confusion_matrix and ConfusionMatrixDisplay evaluate and display the model performance.
# classification_report evaluate the performance of the classification model.
#
#######################################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay,classification_report
import matplotlib.pyplot as plt

#######################################################################
#
# Dataset Loading ->
#
# This step loads the CSV dataset into a Pandas DataFrame, 
# so that it can be analyzed and used for machine learning.
#
#######################################################################

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

print("Dataset loaded successfully")

#######################################################################
#
# Data Analysis ->
#
# This step helps us understand the dataset.
# shape - Number of rows and columns.
# len - Length of data.
# columns - Column names.
# dtypes - Data type of each column.
# describe() - Statistical summary (mean, min, max, etc.).
# isnull().sum() - Checks for missing values.
# value_count() - Returns the no. of distinct values in particular column.
#  
#######################################################################

print("Shape of Dataset : ",df.shape)

print("Length of Dataset : ",len(df))

print("Column names : ",df.columns)

print("Datatypes of each columns : \n",df.dtypes)

print("Missing values per column : \n",df.isnull().sum())

print("Distribution of FinalResult : \n",df["FinalResult"].value_counts())

print("Statistical Report of Dataset : \n",df.describe())

#######################################################################
#
# Decide Independent & Dependent Variables ->
#
# X is Independent Variable.
# Y is Dependent Variable.
#
#######################################################################

feature_columns = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_columns]
Y = df["FinalResult"]

print("Shape of Independent Variables : ",X.shape)
print("Shape of Dependent Variables : ",Y.shape)

#######################################################################
#
# Visualization of the dataset ->
#
#######################################################################

print("Visualization of Dataset")

# Scatter Plot
plt.figure(figsize=(7,5))

for fr in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == fr]
    plt.scatter(temp["StudyHours"], temp["AssignmentsCompleted"], label = fr)

plt.title("Student Case Study")

plt.xlabel("StudyHours")
plt.ylabel("AssignmentsCompleted")

plt.legend()
plt.grid()
plt.show()

#######################################################################
#
# Split the dataset for training and testing ->
#
# X_train -      Features for training the model.
# Y_train -      Labels for training the model.
# X_test -       Features for testing the model.
# Y_test -       Labels for testing the model.
# test_size -    Specifies how much of the dataset is used for testing. 
# random_state - Ensures the same split every time.
#
#######################################################################

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("Shape of X_train : ",X_train.shape)
print("Shape of X_test : ",X_test.shape)
print("Shape of Y_train : ",Y_train.shape)
print("Shape of Y_test : ",Y_test.shape)

#######################################################################
#
# Built the model ->
#
#######################################################################

model = DecisionTreeClassifier()

#######################################################################
#
# Train the model ->
# .fit - Used to train the model.
#
#######################################################################

model.fit(X_train,Y_train)

print("Model trained successfully")

#######################################################################
#
# Test the model ->
# .predict - Used to test the model.
#
#######################################################################

Y_pred = model.predict(X_test)

print("Model testing done")

print("Actual Values : ")
print(Y_test)

print("Predicted Values : ")
print(Y_pred)

#######################################################################
#
# Accuracy Calculation ->
# accuracy_score - Used to calculate the accuracy of predicted values & actual values.
#
#######################################################################

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of the model : ",accuracy*100)

#######################################################################
#
# Confusion Matrix generation ->
# confusion_matrix - Used to calculate the confusion matrix of predicted values & actual values.
#
#######################################################################

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix : \n",cm)

#######################################################################
#
# Classification Report ->
# classification_report - Used to evaluate the performance of classification model.
#
#######################################################################

print("Classification Report")
print(classification_report(Y_test,Y_pred))

#######################################################################
#
# Display Confusion Matrix ->
# 
#######################################################################

display_cm = ConfusionMatrixDisplay(confusion_matrix=cm)

display_cm.plot()

plt.show()