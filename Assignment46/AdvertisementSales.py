import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,root_mean_squared_error,r2_score

def SalesPredictor(csvfilename):
    border = "-"*50
    df = pd.read_csv(csvfilename)

    print(border)
    print("First 5 entries of dataset : ")
    print(border)

    print(df.head())

    print(border)
    print("Sum of all Null Values : ")
    print(border)
    print(df.isnull().sum())

    print(border)
    print("Removing the Unnamed: 0 column : ")

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(border)
    print(df.head())
    print(border)

    print("Statistical Report of Dataset : ")
    print(border)
    print(df.describe())

    print(border)
    print("Correlation")
    print(border)

    print(df.corr())
    print(border)

    print("Shape of Dataset : ",df.shape)
    print(border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Shape of Independent Variables : ",X.shape)
    print(border)

    print("Shape of Dependent Variables : ",Y.shape)
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    print("Training features : ",X_train.shape)
    print("Training label : ",X_test.shape)
    print("Testing features : ",Y_train.shape)
    print("Testing label : ",Y_test.shape)

    print(border)
    print("Built the model : ")

    model = LinearRegression()

    print(border)
    print("Model build successfully...")
    print(border)

    print("Training the model : ")

    model = model.fit(X_train,Y_train)

    print(border)
    print("Model trained successfully...")
    print(border)

    print("Testing the model : ")

    Y_pred = model.predict(X_test)

    print(border)
    print("Expected Output of First 4 Testing Features : ")
    print(Y_test[:4])

    print(border)
    print("Predicted Output of First 4 Testing Features : ")
    print(Y_pred[:4])

    print(border)
    print("Evaluate the model : ")
    print(border)

    MSE = mean_squared_error(Y_test,Y_pred)
    print("Mean Squared Error : ",MSE)

    RMSE = root_mean_squared_error(Y_test,Y_pred)
    print("Root Mean Squared Error : ",RMSE)

    R2 = r2_score(Y_test,Y_pred)
    print("R2 Score : ",R2)

    print(border)
    print("Display the Coefficient : ")
    print(border)

    print("Coefficient of TV : ",model.coef_[0])
    print("Coefficient of Radio : ",model.coef_[1])
    print("Coefficient of Newspaper : ",model.coef_[2])

    print(border)

    print("Displaying Intercept : ")
    print("Intercept : ",model.intercept_)
    print(border)

def main():
    SalesPredictor("Advertising.csv")

if __name__ == "__main__":
    main()