from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report)

def EvaluateModel(model, X_test_scaled, Y_test):

    print("\n----- Model Evaluation -----")

    Y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("\nAccuracy:", accuracy * 100, "%")

    cm = confusion_matrix(Y_test, Y_pred)

    print("\nConfusion Matrix:")
    print(cm)

    report = classification_report(Y_test,Y_pred,target_names=["Malignant", "Benign"])
    
    print("\nClassification Report:")
    print(report)

    print("\n----- OBSERVATIONS -----")

    print("""
    1. The Breast Cancer dataset was successfully loaded and processed.
    2. The data was divided into training and testing datasets.
    3. Feature scaling was performed using StandardScaler.
    4. Logistic Regression was used to classify tumors.
    5. The model performance was evaluated using Accuracy,
    Confusion Matrix, Precision, Recall and F1-Score.
    """)

    print("\n----- CONCLUSION -----")

    print("""
    The machine learning model was successfully developed
    to predict whether a tumor is Malignant or Benign.

    Based on the evaluation results, the Logistic Regression
    model provides effective predictions for the Breast Cancer
    dataset.
    """)
