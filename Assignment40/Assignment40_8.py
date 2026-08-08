# Importing Required Libraries ->

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Dataset Loading ->

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

print("Dataset loaded successfully")

# Data Analysis ->

print("Shape of Dataset : ",df.shape)

print("Length of Dataset : ",len(df))

print("Column names : ",df.columns)

print("Datatypes of each columns : \n",df.dtypes)

print("Missing values per column : \n",df.isnull().sum())

print("Distribution of FinalResult : \n",df["FinalResult"].value_counts())

print("Statistical Report of Dataset : \n",df.describe())

# Decide Independent & Dependent Variables ->

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

# Split the dataset for training and testing ->

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("Shape of X_train : ",X_train.shape)
print("Shape of X_test : ",X_test.shape)
print("Shape of Y_train : ",Y_train.shape)
print("Shape of Y_test : ",Y_test.shape)

# Built the model ->

model = DecisionTreeClassifier()

# Train the model ->

model.fit(X_train,Y_train)

print("Model trained successfully")

# Test the model ->

Y_pred = model.predict(X_test)

print("Model testing done")

print("Actual Values : ")
print(Y_test)

print("Predicted Values : ")
print(Y_pred)

# Decision Tree Visualization ->

plt.figure(figsize=(10,20))

plot_tree(model,feature_names=feature_columns,class_names=["Pass","Fail"],filled=True)

plt.title("Decision Tree Visualization")

plt.show()

#######################################################
# 1) Which feature appears at the root node ?
# -> PreviousScore is root feature.
# 
# 2) Why do you think that feature was selected first ?
# -> The feature at the root node is selected because it provides the best split of training data.
#    It reduces impurity the most and helps Decision Tree to distinguish between Pass(1) and Fail(0) students.
#######################################################