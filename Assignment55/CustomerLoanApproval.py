import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

def main():
    border = "-"*60

    print(border)
    print("Customer Loan Approval System")
    print(border)

    df = pd.read_csv("Customer_Loan_Approval.csv")

    print("Dataset Loaded Successfully")
    print(border)

    print("First 5 entries of Dataset : ")
    print(border)
    print(df.head())
    print(border)

    print("Shape of Dataset : ")
    print(df.shape)
    print(border)

    print("Missing Values in Dataset : ")
    print(border)
    print(df.isnull().sum())
    print(border)

    print("Seperating Input and Output Variables : ")
    print(border)

    X = df.drop("LoanApproved",axis=1)
    Y = df["LoanApproved"]

    print("X Shape : ",X.shape)
    print("Y Shape : ",Y.shape)
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Splitting  Dataset into Training and Testing Data : ")
    print(border)

    print("Shape of Training Features : ",X_train.shape)
    print("Shape of Training Labels : ",X_test.shape)
    print("Shape of Testing Features : ",Y_train.shape)
    print("Shape of Testing Labels : ",Y_test.shape)
    print(border)

    print("Feature Scaling")
    print(border)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("First 5 Scaled Entries of Training : \n")
    print(X_train_scaled[:5])

    print("\nFirst 5 Scaled Entries of Testing : \n")
    print(X_test_scaled[:5])
    
    print(border)

    print("Built the Logistic Regression Model : ")
    print(border)

    modelLog = LogisticRegression(max_iter=1000)

    modelLog = modelLog.fit(X_train_scaled,Y_train)

    Y_Pred = modelLog.predict(X_test_scaled)

    LR_accuracy = accuracy_score(Y_test,Y_Pred)

    print(f"Accuracy Using Logistic Regression : {LR_accuracy*100} %")

    print(border)
    print("Built the Decision Tree Classifier Model : ")
    print(border)

    modelDT = DecisionTreeClassifier(random_state=42)

    modelDT = modelDT.fit(X_train_scaled,Y_train)

    Y_Pred = modelDT.predict(X_test_scaled)

    DT_accuracy = accuracy_score(Y_test,Y_Pred)

    print(f"Accuracy Using Decision Tree : {DT_accuracy*100} %")

    print(border)
    print("Built the K-Nearest Neighbors (KNN) Model : ")
    print(border)

    modelKNN = KNeighborsClassifier(n_neighbors=5)

    modelKNN = modelKNN.fit(X_train_scaled,Y_train)

    Y_Pred = modelKNN.predict(X_test_scaled)

    KNN_accuracy = accuracy_score(Y_test,Y_Pred)

    print(f"Accuracy Using KNN : {KNN_accuracy*100} %")

    print(border)

    print("Built the Hard Voting Classifier Model : ")
    print(border)

    HardVotingModel = VotingClassifier(
        estimators=[
            ('logistic',modelLog),
            ('decision_tree',modelDT),
            ('knn',modelKNN),
        ],
        voting='hard'
    )

    HardVotingModel = HardVotingModel.fit(X_train_scaled,Y_train)

    Y_Pred = HardVotingModel.predict(X_test_scaled)

    HV_accuracy = accuracy_score(Y_test,Y_Pred)

    print(f"Accuracy Using Hard Voting : {HV_accuracy*100} %")

    print(border)

    print("Built the Soft Voting Classifier Model : ")
    print(border)

    SoftVotingModel = VotingClassifier(
        estimators=[
            ('logistic',modelLog),
            ('decision_tree',modelDT),
            ('knn',modelKNN),
        ],
        voting='soft'
    )

    SoftVotingModel = SoftVotingModel.fit(X_train_scaled,Y_train)

    Y_Pred = SoftVotingModel.predict(X_test_scaled)

    SV_accuracy = accuracy_score(Y_test,Y_Pred)

    print(f"Accuracy Using Soft Voting : {SV_accuracy*100} %")

    print(border)

    print("Model Comparison")
    print(border)

    results = pd.DataFrame({
        "Model":[
            "Logistic Regression",
            "Decision Tree",
            "KNN",
            "Hard Voting",
            "Soft Voting"
            ],
        "Accuracy":[
            LR_accuracy*100,
            DT_accuracy*100,
            KNN_accuracy*100,
            HV_accuracy*100,
            SV_accuracy*100
        ]
    })

    print(results)
    print(border)

    models = {
        "Logistic Regression" : LR_accuracy,
        "Decision Tree" : DT_accuracy,
        "KNN" : KNN_accuracy,
        "Hard Voting" : HV_accuracy,
        "Soft Voting" : SV_accuracy
    }

    best_model = max(models,key=models.get)
    print("Best Model")
    print(border)
    print("Recommended Model : ",best_model)
    print("Accuracy : ",models[best_model]*100,"%")
    print(border)

if __name__ == "__main__":
    main()