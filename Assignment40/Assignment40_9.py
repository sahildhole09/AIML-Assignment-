import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Dataset = "student_performance_ml.csv"
df = pd.read_csv(Dataset)

print("Dataset loaded successfully")

df["PerformanceIndex"] = (df["StudyHours"] * 2 + df["Attendance"])

print("PerformanceIndex created successfully,\n")

print(df[["StudyHours","Attendance","PerformanceIndex"]])

feature_columns = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "PerformanceIndex"
]

X = df[feature_columns]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train,Y_train)

print("\nModel trained successfully")

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test,Y_pred)

print("\nTesting Accuracy : ",accuracy*100,"%")

Y_train_pred = model.predict(X_train)

train_accuracy = accuracy_score(Y_train,Y_train_pred)

print("\nTraining Accuracy : ",accuracy*100,"%")

print("\nActual Values : ")
print(Y_test.values)

print("\nPredicted Values : ")
print(Y_pred)

if(accuracy == 1.0):
    print("\nObservation:")
    print("The model achieved 100% testing accuracy.")
    print("Adding PerformanceIndex did not improve the accuracy because model already performing")
    print("very well with the original features.")
else:
    print("\nObservation:")
    print("The model accuracy after adding PerformanceIndex is : ",accuracy*100,"%")