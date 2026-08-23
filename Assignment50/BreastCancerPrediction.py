from DataLoading import LoadData
from Preprocessing import PreprocessData
from ModelBuilding import BuildModel
from Evaluation import EvaluateModel

def main():

    df = LoadData()

    X_train_scaled, X_test_scaled, Y_train, Y_test = PreprocessData(df)

    model = BuildModel(X_train_scaled,Y_train)

    EvaluateModel(model,X_test_scaled,Y_test)

if __name__ == "__main__":
    main()