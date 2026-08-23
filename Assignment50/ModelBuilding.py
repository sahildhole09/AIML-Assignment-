from sklearn.linear_model import LogisticRegression

def BuildModel(X_train_scaled, Y_train):

    print("\n----- Model Building -----")

    model = LogisticRegression(max_iter=10000,random_state=42)

    model.fit(X_train_scaled,Y_train)

    print("Model trained successfully.")

    return model