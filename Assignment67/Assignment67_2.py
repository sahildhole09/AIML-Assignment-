import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


def create_dataset():

    df = pd.DataFrame({
        "Income": [25000,40000,60000,20000,80000,
                   35000,18000,90000,30000,70000],
        "CreditScore": [600,700,750,550,800,
                        650,500,850,580,780],
        "LoanAmount": [200000, 300000, 500000, 150000, 700000,
                       250000, 100000, 800000, 200000, 600000],
        "ExistingEMI": [10000, 8000, 12000, 15000, 10000,
                        9000, 12000, 15000, 14000, 10000],
        "EmploymentStatus": [0, 1, 1, 0, 1,
                            1, 0, 1, 0, 1],
        "LoanApproval": [0, 1, 1, 0, 1,
                        1, 0, 1, 0, 1]
                        })

    print("Dataframe is : \n")
    print(df)

    print("\nDataframe created successfully")

    return df

def data_preprocessing(df):
    X = df.drop("LoanApproval",axis=1)

    Y = df["LoanApproval"]

    # EmploymentStatus is already encoded : 
    # 0 = Not Stable
    # 1 = Stable

    return X,Y

def data_splitting(X,Y):

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42,stratify=Y)

    return X_train,X_test,Y_train,Y_test

def data_scaling(X_train,X_test):

    scalar = StandardScaler()

    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    return scalar,X_train_scaled,X_test_scaled

def create_model(X_train_scaled,Y_train,X_test_scaled,Y_test):
    
    model = MLPClassifier(
        hidden_layer_sizes=(10,5),
        activation='relu',
        solver='adam',
        learning_rate_init=0.1,
        max_iter=1000,
        random_state=42
    )

    model.fit(X_train_scaled,Y_train)
    print("\nModel Trained Successfully")

    Y_pred = model.predict(X_test_scaled)
    print("\nModel Tested Successfully")

    return model,Y_pred

def evaluate_model(Y_test,Y_pred):

    accuracy = accuracy_score(Y_test,Y_pred)
    print("\nAccuracy : ",accuracy,"%")

    cm = confusion_matrix(Y_test,Y_pred)
    print("\nConfusion Matrix : ")
    print(cm)

    report = classification_report(Y_test,Y_pred)
    print("\nClassification Report : ")
    print(report)

def new_prediction(scalar,model):

    new_applicant = pd.DataFrame({
        "Income": [55000],
        "CreditScore": [720],
        "LoanAmount": [400000],
        "ExistingEMI": [10000],
        "EmploymentStatus": [1]
        })

    print("\nNew Applicant : ")
    print(new_applicant)

    new_applicant_scaled = scalar.transform(new_applicant)

    prediction = model.predict(new_applicant_scaled)

    probability = model.predict_proba(new_applicant_scaled)

    if prediction[0] == 1 :
        print("\nPrediction : Loan Approved")
    else:
        print("\nPrediction : Loan Rejected")

    print("\nProbability of Rejection : ",probability[0][0])
    print("\nProbability of Approval : ",probability[0][1])
    
def main():    
    df = create_dataset()

    X,Y = data_preprocessing(df)

    X_train,X_test,Y_train,Y_test = data_splitting(X,Y)

    scalar,X_train_scaled,X_test_scaled = data_scaling(X_train,X_test)

    model,Y_pred = create_model(X_train_scaled,Y_train,X_test_scaled,Y_test)

    evaluate_model(Y_test,Y_pred)

    new_prediction(scalar,model)
    
if __name__ == "__main__":
     main()