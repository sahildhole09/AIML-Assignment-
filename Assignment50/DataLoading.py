from sklearn.datasets import load_breast_cancer
import pandas as pd

def LoadData():

    print("----- Loading Breast Cancer Dataset -----")

    Data = load_breast_cancer()

    df = pd.DataFrame(Data.data,columns=Data.feature_names)

    df["target"] = Data.target

    print("\n Dataset Shape:")
    print(df.shape)

    print("\n First 5 Records:")
    print(df.head())

    print("\n Dataset Information:")
    print(df.info())

    print("\n Summary Statistics:")
    print(df.describe())

    print("\n Target Distribution:")
    print(df["target"].value_counts())

    print("\n Target:")
    print("0 = Malignant")
    print("1 = Benign")

    return df