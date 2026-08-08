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

# With max_depth = None 

model1 = DecisionTreeClassifier(max_depth=None)

model1.fit(X_train,Y_train)

Y_pred = model1.predict(X_test)

print("Actual Values : ")
print(Y_test)

print("Predicted Values : ")
print(Y_pred)

accuracy1 = accuracy_score(Y_test,Y_pred)
print("Accuracy of the model : ",accuracy1*100)

# With max_depth = 1

model2 = DecisionTreeClassifier(max_depth=1)

model2.fit(X_train,Y_train)

Y_pred = model2.predict(X_test)

print("Actual Values : ")
print(Y_test)

print("Predicted Values : ")
print(Y_pred)

accuracy2 = accuracy_score(Y_test,Y_pred)
print("Accuracy of the model : ",accuracy2*100)

# With max_depth = 3

model3 = DecisionTreeClassifier(max_depth=3)

model3.fit(X_train,Y_train)

Y_pred = model3.predict(X_test)

print("Actual Values : ")
print(Y_test)

print("Predicted Values : ")
print(Y_pred)

accuracy3 = accuracy_score(Y_test,Y_pred)
print("Accuracy of the model : ",accuracy3*100)

# All three models give the same testing accuracy.
# Increasing the value of max_depth does not improve the model's performance.
# The dataset is simple enough that different tree depths produce the same results.