import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def CheckAccuracy(X,Y):
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("\nAccuracy with different K values")

    for K in range(1,16):
        model = KNeighborsClassifier(n_neighbors=K)

        model.fit(X_train,Y_train)

        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test,Y_pred)

        print("K : ",K,"Accuracy : ",accuracy*100,"%")

def KKNClassifier():
    border = "-"*50

    Dataset = "MarvellousInfosystems_PlayPredictor.csv"

    df = pd.read_csv(Dataset)
    
    print("First 5 records : ")
    print(df.head())

    print("\nShape of Dataset : ")
    print(df.shape)

    le_wether = LabelEncoder()
    le_temperature = LabelEncoder()
    le_play = LabelEncoder()

    df["Wether"] = le_wether.fit_transform(df["Wether"])
    df["Temperature"] = le_temperature.fit_transform(df["Temperature"])
    df["Play"] = le_play.fit_transform(df["Play"])

    print("\nEncoded Dataset : ")
    print(df.head())

    X = df[["Wether","Temperature"]]
    Y = df["Play"]

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X,Y)

    wether_input = "Sunny"
    temp_input = "Cool"

    wether_encoded = le_wether.transform([wether_input])[0]
    temp_encoded = le_temperature.transform([temp_input])[0]

    test_data = [[wether_encoded,temp_encoded]]

    prediction = model.predict(test_data)

    result = le_play.inverse_transform(prediction)

    print("\nPrediction")
    print("Wether        :",wether_input)
    print("Temperature   :",temp_input)
    print("Play          :",result[0])

    CheckAccuracy(X,Y)

def main():
    KKNClassifier()

if __name__ == "__main__":
    main()