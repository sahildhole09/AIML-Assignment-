import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def create_dataset():

    df = pd.DataFrame({
        "Age" : [25,30,45,50,28,35,48,52,27,42],
        "MonthlyCharges" : [500,700,1200,1500,600,800,1400,1600,550,1300],
        "Tenure" : [12,24,6,5,18,30,4,3,20,8],
        "Complaints" : [1,0,5,6,1,0,7,8,0,4],
        "SupportCalls" : [2,1,8,10,1,0,9,12,1,7],
        "Target" : [0,0,1,1,0,0,1,1,0,1]
    }
    )

    feature_col = ["Age", "MonthlyCharges", "Tenure", "Complaints", "SupportCalls"]

    print("Dataframe is : \n")
    print(df)

    print("\nDataframe created successfully")

    return df,feature_col

def data_cleaning(df,feature_col):

    print("\nMissing Values : ")
    print(df.isnull().sum())

    df.drop_duplicates(inplace=True)
    
    for column in feature_col:
        df.loc[df[column] < 0,column] = np.nan

    for column in feature_col:
        df[column] = df[column].fillna(df[column].median())

    df = df[df["Target"].isin([0,1])]

    print("\nCleaned Dataframe : ")
    print(df)

    return df

def data_splitting(df):

    X = df.drop("Target",axis=1)
    Y = df["Target"]

    print(X.shape)
    print(Y.shape)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("\nData Splitted Successfully")

    return X_train,X_test,Y_train,Y_test

def data_scaling(X_train,X_test):
    scalar = StandardScaler()

    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    return X_train_scaled, X_test_scaled,scalar

def create_model(X_train_scaled,X_test_scaled,Y_train,Y_test):

    model = MLPClassifier(
        hidden_layer_sizes=(6,3),
        activation='relu',
        solver='adam',
        max_iter=1000,
        random_state=42
    )

    print("\nTrain the model")

    model.fit(X_train_scaled,Y_train)

    print("\nModel training completed")
    
    Y_pred = model.predict(X_test_scaled)

    print("\nModel testing completed")

    print("\nExpected Output : ")
    print(Y_test)

    print("\nPredicted Output : ")
    print(Y_pred)

    return model,Y_test,Y_pred

def evaluate_model(Y_test,Y_pred):

    accuracy = accuracy_score(Y_test,Y_pred)

    print("\nAccuracy is : ",accuracy,"%\n")

def new_prediction(feature_col,scalar,model):
    new_customer = pd.DataFrame([
        [46, 1450, 5, 6, 9]],
        columns=feature_col)

    print("\nNew Customer:")
    print(new_customer)

    new_customer_scaled = scalar.transform(new_customer)

    prediction = model.predict(new_customer_scaled)

    if prediction[0] == 0:
        print("\nPrediction: Customer will stay")
    else:
        print("\nPrediction: Customer may leave")

def main():    
    df,feature_col = create_dataset()
    df = data_cleaning(df,feature_col)
    X_train,X_test,Y_train,Y_test = data_splitting(df)
    X_train_scaled, X_test_scaled, scalar = data_scaling(X_train,X_test)
    model,Y_test,Y_pred = create_model(X_train_scaled,X_test_scaled,Y_train,Y_test)
    evaluate_model(Y_test,Y_pred)
    new_prediction(feature_col,scalar,model)
    
if __name__ == "__main__":
     main()