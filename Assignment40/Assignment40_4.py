# Importing Required Libraries ->

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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

new_students = pd.DataFrame({
    "StudyHours" : [2,4,5,6,8],
    "Attendance" : [65,75,80,85,92],
    "PreviousScore" : [45,55,60,65,75],
    "AssignmentsCompleted" : [3,5,6,7,9],
    "SleepHours" : [5,6,7,7,8]
})

new_pred = model.predict(new_students)

new_students["PredictedResult"] = new_pred

print(new_students)

