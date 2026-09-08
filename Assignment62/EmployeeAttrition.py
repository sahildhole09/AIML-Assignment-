import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

import matplotlib.pyplot as plt

def data_loading():
    data = pd.read_csv("Employee_Attrition.csv")

    print("Data gets loaded successfully...!")

    print("Shape of Dataset : ")
    print(data.shape)

    print("Columns of Dataset : ")
    print(data.columns)

    print("First 5 entries of dataset : ")
    print(data.head())

    return data

def data_analysis(data):
    print("Sum of missing values of dataset : ")
    print(data.isnull().sum())

    num_col = data.select_dtypes(include="number").columns
    print("Numerical Columns : ",list(num_col))

    cat_col = data.select_dtypes(include="object").columns
    print("Categorical Columns : ",list(cat_col))

    le = LabelEncoder()
    data["OverTime"] = le.fit_transform(data["OverTime"])

    data["Attrition"] = le.fit_transform(data["Attrition"])

    return le

def variable_seperation(data):
    X = data.drop("Attrition",axis=1)
    Y = data["Attrition"]

    print("Shape of Independent Variable : ")
    print(X.shape)

    print("Shape of Dependent Variable : ")
    print(Y.shape)

    return X,Y

def data_splitting(X,Y):
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.50,random_state=42)

    print("Shape of Training Features : ",X_train.shape)
    print("Shape of Testing Features : ",X_test.shape)
    print("Shape of Training Labels : ",Y_train.shape)
    print("Shape of Testing Labels : ",Y_test.shape)

    return X_train,X_test,Y_train,Y_test

def data_scaling(X_train,X_test):

    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Scaled first 5 training features :")
    print(X_train_scaled[:5])

    print("Scaled first 5 testing features :")
    print(X_test_scaled[:5])

    return X_train_scaled,X_test_scaled,scalar

def create_model(X_train_scaled,X_test_scaled,Y_train):
    model = MLPClassifier(
        hidden_layer_sizes=(10,6),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    print("Model built successfully...")

    model.fit(X_train_scaled,Y_train)

    print("Model Trained Successfully...")

    Y_train_pred = model.predict(X_train_scaled)

    Y_test_pred = model.predict(X_test_scaled)

    print("Model Tested Successfully...")

    return model,Y_train_pred,Y_test_pred

def evaluate_model(model,Y_train,Y_test,Y_train_pred,Y_test_pred):
    print("Number of Iterations required for training : ")
    print(model.n_iter_)

    training_accuracy = accuracy_score(Y_train,Y_train_pred)
    print(f"Training Accuracy : {training_accuracy*100} %")

    testing_accuracy = accuracy_score(Y_test,Y_test_pred)
    print(f"Testing Accuracy : {testing_accuracy*100} %")

    cm = confusion_matrix(Y_test,Y_test_pred)
    print("Confusion Matrix : \n",cm)

    plt.plot(model.loss_curve_)

    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.title("MLP Training Loss Curve")
    plt.show()

def PredictAttrition(model,scalar,le):

    new_emp = pd.DataFrame([
        [25, 30000, 1, 2, 2, 3, 4, "No", 1, 3],    
        [58, 120000, 1, 20, 25, 1, 1, "Yes", 4, 1], 
        [29, 35000, 3, 5, 3, 4, 4, "No", 1, 4],  
        [48, 95000, 1, 20, 22, 1, 2, "Yes", 5, 1],
        [34, 50000, 7, 10, 5, 4, 3, "No", 2, 3]
        ],
        columns=[
            "Age",
            "MonthlyIncome",
            "YearsAtCompany",
            "TotalWorkingYears",
            "DistanceFromHome",
            "JobSatisfaction",
            "WorkLifeBalance",
            "OverTime",
            "NumCompaniesWorked",
            "TrainingTimesLastYear"
            ])

    new_emp["OverTime"] = le.transform(new_emp["OverTime"])

    new_emp_scaled = scalar.transform(new_emp)
    
    new_emp_pred = model.predict(new_emp_scaled)

    new_emp_pred = model.predict_proba(new_emp_scaled)

    for emp in range(len(new_emp_pred)):
        print("Employee",emp+1,"Stay : ",round(new_emp_pred[emp][0]*100,2),"%", \
        "Leave : ",round(new_emp_pred[emp][1]*100,2),"%")
        
        if(new_emp_pred[emp][1]>new_emp_pred[emp][0]):
            print("Prediction : Employee is likely to Leave")
        else:
            print("Prediction : Employee is likely to Stay")

def main():
    loading_data = data_loading()

    le = data_analysis(loading_data)

    X,Y = variable_seperation(loading_data)

    X_train,X_test,Y_train,Y_test = data_splitting(X,Y)

    X_train_scaled,X_test_scaled,scalar = data_scaling(X_train,X_test)

    model,Y_train_pred,Y_test_pred = create_model(X_train_scaled,X_test_scaled,Y_train)

    model_evaluation = evaluate_model(model,Y_train,Y_test,Y_train_pred,Y_test_pred)

    new_emp = PredictAttrition(model,scalar,le)

if __name__ == "__main__":
    main()

########################################################################
# Observation ->
# The model achieved 88.2 % training accuracy and 78.4 % testing accuracy.
# The difference of 9.8 % indicates that the model performs better on training data than unseen data.
########################################################################
# Conclusion ->
# The Model is suffering from Overfitting,
# as its testing performance is considerably lower than its training performance.
########################################################################