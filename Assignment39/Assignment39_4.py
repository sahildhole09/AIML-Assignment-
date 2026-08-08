import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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

# Test the model

Y_pred = model.predict(X_test)

print("Model testing done")

print("Actual Values : ")
print(Y_test)

print("Predicted Values : ")
print(Y_pred)

# Accuracy

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of the model : ",accuracy*100)

# Confusion Matrix 

cm = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix : \n",cm)

# Display Confusion Matrix

display_cm = ConfusionMatrixDisplay(confusion_matrix=cm)

display_cm.plot()

plt.show()

###########################################################
#
# True Positive - Correctly predicted positive samples.
# True Negative - Correctly predicted negative samples.
# False Positive - Incorrectly predicted positive when actual is negative.
# False Negative - Incorrectly predicted negative when actual is positive.
#
###########################################################