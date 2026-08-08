import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Dataset Loading

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

print("Dataset loaded successfully")

# Data Analysis (EDA)

print("Shape of Dataset : ",df.shape)

print("Length of Dataset : ",len(df))

print("Column names : ",df.columns)

print("Datatypes of each columns : \n",df.dtypes)

print("Missing values per column : \n",df.isnull().sum())

print("Distribution of FinalResult : \n",df["FinalResult"].value_counts())

print("Statistical Report of Dataset : \n",df.describe())

# Decide Independent & Dependent Variables

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

# Split the dataset for training and testing

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("Shape of X_train : ",X_train.shape)
print("Shape of X_test : ",X_test.shape)
print("Shape of Y_train : ",Y_train.shape)
print("Shape of Y_test : ",Y_test.shape)

# Built the model

model = DecisionTreeClassifier()

# Train the model

model.fit(X_train,Y_train)

print("Model trained successfully")

# Training accuracy

Y_train_pred = model.predict(X_train)

print("Actual Values : ")
print(Y_train)

print("Predicted Values : ")
print(Y_train_pred)

training_accuracy = accuracy_score(Y_train,Y_train_pred)
print("Testing Accuracy of the model : ",training_accuracy*100)

# Testing accuracy

Y_test_pred = model.predict(X_test)

print("Actual Values : ")
print(Y_test)

print("Predicted Values : ")
print(Y_test_pred)

testing_accuracy = accuracy_score(Y_test,Y_test_pred)
print("Testing Accuracy of the model : ",testing_accuracy*100)

# The traing accuracy and testing accuracy are both 100%. This indicates that the model has classified all training and testing samples correctly.
# Therefore, the model is well-fitted on this dataset.

