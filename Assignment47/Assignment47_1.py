import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main():
    X = np.array([[1],[2],[3],[4],[5]])
    Y = np.array([50,55,60,65,70])

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = LinearRegression()

    model = model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    print("Coefficient : ",model.coef_)

    print("Intercept : ",model.intercept_)

if __name__ == "__main__":
    main()