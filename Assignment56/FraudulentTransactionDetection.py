import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

def DecisionTree(border,X_train,X_test,Y_train,Y_test):
    print("Creation of Decision Tree Classification Model")
    print(border)

    model = DecisionTreeClassifier(random_state=42)

    model = model.fit(X_train,Y_train)

    Y_Pred = model.predict(X_test)

    print("Model Evaluation using Decision Tree Classifier")
    print(border)

    accuracy = accuracy_score(Y_test,Y_Pred)
    print(f"Accuracy : {accuracy*100} %\n")
 
    precision = precision_score(Y_test,Y_Pred)
    print(f"Precision : {precision}\n")

    recall = recall_score(Y_test,Y_Pred)
    print(f"Recall : {recall}\n")

    f1score = f1_score(Y_test,Y_Pred)
    print(f"F1_Score : {f1score}\n")

    cm = confusion_matrix(Y_test,Y_Pred)
    print(f"Confusion Matrix : ")
    print(cm)

    report = classification_report(Y_test,Y_Pred)
    print("\nClassification Report : ")
    print(report)

    print(border)

    return accuracy

def Bagging(border,X_train,X_test,Y_train,Y_test):
    print("Creation of Bagging Classification Model")
    print(border)

    base_model = DecisionTreeClassifier(random_state=42)

    model = BaggingClassifier(
        estimator=base_model,
        n_estimators=10,
        random_state=42
        )
    
    model = model.fit(X_train,Y_train)

    Y_Pred = model.predict(X_test)

    print("Model Evaluation using Bagging Classifier")
    print(border)

    accuracy = accuracy_score(Y_test,Y_Pred)
    print(f"Accuracy : {accuracy*100} %\n")

    precision = precision_score(Y_test,Y_Pred)
    print(f"Precision : {precision}\n")

    recall = recall_score(Y_test,Y_Pred)
    print(f"Recall : {recall}\n")

    f1score = f1_score(Y_test,Y_Pred)
    print(f"F1_Score : {f1score}\n")

    cm = confusion_matrix(Y_test,Y_Pred)
    print(f"Confusion Matrix : ")
    print(cm)

    report = classification_report(Y_test,Y_Pred)
    print("\nClassification Report : ")
    print(report)

    print(border)

    return accuracy

def RandomForest(border,X_train,X_test,Y_train,Y_test):
    print("Creation of Random Forest Classification Model")
    print(border)

    model = RandomForestClassifier(
        n_estimators=10,
        random_state=42
    )

    model = model.fit(X_train,Y_train)

    Y_Pred = model.predict(X_test)

    print("Model Evaluation using Random Forest Classifier")
    print(border)

    accuracy = accuracy_score(Y_test,Y_Pred)
    print(f"Accuracy : {accuracy*100} %\n")

    precision = precision_score(Y_test,Y_Pred)
    print(f"Precision : {precision}\n")

    recall = recall_score(Y_test,Y_Pred)
    print(f"Recall : {recall}\n")

    f1score = f1_score(Y_test,Y_Pred)
    print(f"F1_Score : {f1score}\n")

    cm = confusion_matrix(Y_test,Y_Pred)
    print(f"Confusion Matrix : ")
    print(cm)

    report = classification_report(Y_test,Y_Pred)
    print("\nClassification Report : ")
    print(report)

    print(border)

    return accuracy

def Boosting(border,X_train,X_test,Y_train,Y_test):
    print("Creation of Boosting Classification Model")
    print(border)

    model = AdaBoostClassifier(
        n_estimators=50,
        learning_rate=1.0,
        random_state=42
    )

    model = model.fit(X_train,Y_train)

    Y_Pred = model.predict(X_test)

    print("Model Evaluation using Boosting Classifier")
    print(border)

    accuracy = accuracy_score(Y_test,Y_Pred)
    print(f"Accuracy : {accuracy*100} %\n")

    precision = precision_score(Y_test,Y_Pred)
    print(f"Precision : {precision}\n")

    recall = recall_score(Y_test,Y_Pred)
    print(f"Recall : {recall}\n")

    f1score = f1_score(Y_test,Y_Pred)
    print(f"F1_Score : {f1score}\n")

    cm = confusion_matrix(Y_test,Y_Pred)
    print(f"Confusion Matrix : ")
    print(cm)

    report = classification_report(Y_test,Y_Pred)
    print("\nClassification Report : ")
    print(report)

    print(border)

    return accuracy

def Voting(border,X_train,X_test,Y_train,Y_test):
    print("Creation of Voting Classification Model")
    print(border)

    modeldt = DecisionTreeClassifier(random_state=42)
    modellog = LogisticRegression(max_iter=1000)
    modelknn = KNeighborsClassifier(n_neighbors=5)

    model = VotingClassifier(
        estimators=[
            ('Decision Tree',modeldt),
            ('Logistic',modellog),
            ('knn',modelknn)
        ],
        voting='hard'
    )

    model = model.fit(X_train,Y_train)

    Y_Pred = model.predict(X_test)

    print("Model Evaluation using Voting Classifier")
    print(border)

    accuracy = accuracy_score(Y_test,Y_Pred)
    print(f"Accuracy : {accuracy*100} %\n")

    precision = precision_score(Y_test,Y_Pred)
    print(f"Precision : {precision}\n")

    recall = recall_score(Y_test,Y_Pred)
    print(f"Recall : {recall}\n")

    f1score = f1_score(Y_test,Y_Pred)
    print(f"F1_Score : {f1score}\n")

    cm = confusion_matrix(Y_test,Y_Pred)
    print(f"Confusion Matrix : ")
    print(cm)

    report = classification_report(Y_test,Y_Pred)
    print("\nClassification Report : ")
    print(report)

    print(border)

    return accuracy

def main():
    border = "*"*60

    print(border)
    print("-------- Fraudulent Transaction Detection System --------")
    print(border)

    df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

    print("Dataset Loaded Successfully...")
    print(border)

    print("First 5 entries of Dataset : ")
    print(border)

    print(df.head())
    print(border)

    print("Seperate the Features and Labels")
    print(border)

    X = df.drop("Fraud",axis=1)
    Y = df["Fraud"]

    print("X Shape : ",X.shape)
    print("Y Shape : ",Y.shape)
    print(border)

    print("Splitting the Dataset into Training and Testing Data")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Shape of X_train :",X_train.shape)
    print("Shape of X_test :",X_test.shape)
    print("Shape of Y_train :",Y_train.shape)
    print("Shape of Y_test :",Y_test.shape)
    print(border)

    print("Feature Scaling")
    print(border)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)

    print("First 5 scaled training feature entries\n")
    print(X_train[:5])
    print(border)

    DT_accuracy = DecisionTree(border,X_train,X_test,Y_train,Y_test)

    Bag_accuracy = Bagging(border,X_train,X_test,Y_train,Y_test)

    RF_accuracy = RandomForest(border,X_train,X_test,Y_train,Y_test)

    Boost_accuracy = Boosting(border,X_train,X_test,Y_train,Y_test)

    Voting_accuracy = Voting(border,X_train,X_test,Y_train,Y_test)

    result = pd.DataFrame({
        "Algorithm":[
            "Decision Tree",
            "Bagging",
            "Random Forest",
            "AdaBoost",
            "Voting"
        ],
        "Accuracy":[
            DT_accuracy,
            Bag_accuracy,
            RF_accuracy,
            Boost_accuracy,
            Voting_accuracy
        ]
    })

    print(result)
    print(border)

    models = {
        "Decision Tree":DT_accuracy,
        "Bagging":Bag_accuracy,
        "Random Forest":RF_accuracy,
        "AdaBoost":Boost_accuracy,
        "Voting":Voting_accuracy
    }

    best_model = max(models,key=models.get)
    print("Best Model")
    print(border)
    print("Recommended Model : ",best_model)
    print("Accuracy : ",models[best_model]*100,"%")
    print(border)

if __name__ == "__main__":
    main()