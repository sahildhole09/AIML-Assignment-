# Importing Required Libraries ->

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

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

# Split the dataset for training and testing using random_state = 0 ->

random_states = [0,10,42]

for rs in random_states:
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=rs)
    
    model = DecisionTreeClassifier()

    model.fit(X_train,Y_train)

    print("Model trained successfully")

    Y_pred = model.predict(X_test)

    print("Model testing done")

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Random State : ",rs)
    print("Accuracy : ",accuracy*100,"%")

#############################################################
#
# Random State :  0
# Accuracy :      83.33333333333334 %

# Random State :  10
# Accuracy :      100.0 %

# Random State :  42
# Accuracy :      100.0 %

# The testing accuracy changes when the random_state changes because different random states create different training and testing datasets. 
# In this dataset, random_state=42 gives the highest testing accuracy of 100%.
# random_state does not improve the model itself; it changes how the data is split.
#
#############################################################