import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,precision_score,recall_score,f1_score
import matplotlib.pyplot as plt

def data_load():
    data = pd.read_csv("Loan_Default.csv")

    print("Dataset Loaded Successfully")

    print("First 5 entries of dataset : ")
    print(data.head())

    return data

def data_analysis(data):
    print("Shape of dataset : ")
    print(data.shape)

    print("Columns of dataset : ")
    print(data.columns)

    print("Statical summary of dataset : ")
    print(data.describe())

    print("Sum of missing values of columns : ")
    print(data.isnull().sum())

    print("Duplicate Records : ")
    print(data.duplicated().sum())

    data = data.drop_duplicates()

    print("Count of target values : ")
    print(data["Default"].value_counts())

    print("Count of target values in Percentage : ")
    print(data["Default"].value_counts(normalize=True)*100)

    print("Correlation of dataset : ")
    print(data.corr)

def data_encoding(data):
    cat_col = data.select_dtypes(include="object").columns
    print("Categorical Columns : ",list(cat_col))

    le = LabelEncoder()

    data["PreviousDefault"] = le.fit_transform(data["PreviousDefault"])
    data["HomeOwnership"] = le.fit_transform(data["HomeOwnership"])

    print("Encoded the Categorical Columns Successfully")

    num_col = data.select_dtypes(include="number").columns
    print("Numerical Columns : ",list(num_col))

    return le

def data_splitting(data):
    X = data.drop("Default",axis=1)
    Y = data["Default"]

    print("Shape of Independent Variable (X) : ")
    print(X.shape)

    print("Shape of Dependent Variable (Y) : ")
    print(Y.shape)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print("Shape of Training Independent Variables : ",X_train.shape)
    print("Shape of Training Dependent Variables : ",Y_train.shape)
    print("Shape of Testing Independent Variables : ",X_test.shape)
    print("Shape of Testing Dependent Variables : ",Y_test.shape)

    return X_train,X_test,Y_train,Y_test

def data_scaling(X_train,X_test):

    scalar = StandardScaler()

    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("First 5 entries of scaled training features : ")
    print(X_train_scaled[:5])

def create_model(X_train,X_test,Y_train,Y_test):
    model = MLPClassifier(
        hidden_layer_sizes=(32,16),
        activation="relu",
        solver="adam",
        max_iter=1000,
        learning_rate_init=0.1,
        random_state=42
    )

    print("Model created successfully")

    model.fit(X_train,Y_train)

    print("Model trained successfully")

    Y_pred = model.predict(X_test)

    print("Expected Output : \n",Y_test[:5])
    print("Predicted Output : \n",Y_pred[:5])

    print("Model tested successfully")

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of the model : ",accuracy*100,"%")

    cm = confusion_matrix(Y_test,Y_pred)
    print("Confusion Matrix : \n",cm)

    report = classification_report(Y_test,Y_pred)
    print("Classification Report : \n",report)

    precision = precision_score(Y_test,Y_pred)
    print("Precision : ",precision)

    recall = recall_score(Y_test,Y_pred)
    print("Recall : ",recall)

    F1Score = f1_score(Y_test,Y_pred)
    print("F1 Score : ",F1Score)

    print("Training Loss : ")
    print(model.loss_)

    plt.figure(figsize=(8,5))

    plt.plot(model.loss_curve_)

    plt.title("MLP Training Loss Curve")
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.grid()

    plt.show()

    return model

def new_loan_applicant(model,le):
    new_applicant = pd.DataFrame([[35,60000,25000,700,8,1,1200,48,"No","Mortgage"]],columns=['Age', 'Income', 'LoanAmount', 'CreditScore', 'EmploymentYears',
       'ExistingLoans', 'MonthlyDebt', 'LoanTerm', 'PreviousDefault','HomeOwnership'])
    
    new_applicant["PreviousDefault"] = le.fit_transform(new_applicant["PreviousDefault"])
    new_applicant["HomeOwnership"] = le.fit_transform(new_applicant["HomeOwnership"])
    
    new_applicant_pred = model.predict(new_applicant)

    probability = model.predict_proba(new_applicant)

    print("Prediction of New Applicant : ",new_applicant_pred)
    print("Default Probability : ",probability[0][1]*100,"%")

    if(new_applicant_pred == 0):
        print("Result : LOw Default Risk")
    else:
        print("Result : High Default Risk")

def main():
    data = data_load()

    EDA = data_analysis(data)

    le = data_encoding(data)

    X_train,X_test,Y_train,Y_test = data_splitting(data)

    data_scaling(X_train,X_test)

    model = create_model(X_train,X_test,Y_train,Y_test)

    new_loan_applicant(model,le)

if __name__ == "__main__":
    main()


################################################################################
# Experiment 1 : By Changing Activation Function
#
# The experiment was performed by changing the activation functions to 
# ReLU,Identity, Tanh, and Logistic.
# The results show that Logistic achieved the highest accuracy (73.33%),
# followed by ReLU (72.08%) and Tanh (71.66%).
# Identity gave the lowest accuracy (55.41%).
# Therefore, Logistic was the best-performing activation function for this experiment.
#
################################################################################

################################################################################
# Experiment 2 : By CHanging Hidden Layers
#
# In this experiment, the ReLU activation function was kept constant
# while changing the number of hidden layers and neurons. 
# The (32,16) architecture gave the highest accuracy of 72.08%, while (10,) gave 60.83%. 
# The larger architectures did not improve accuracy, with (20,10) = 65.83%, (50,25) = 67.91%, and (100,50,25) = 63.33%.
# Conclusion :
# The results show that increasing the number of neurons/layers does not always improve model performance. 
# For this dataset, the (32,16) hidden-layer configuration performed best,
# while very large or smaller architectures gave lower accuracy.
#
################################################################################

################################################################################
# Experiment 3 : By Changing Hidden Layers
#
# In this experiment, the ReLU activation function was kept constant
# while changing the learning rate. The highest accuracy was 73.33% at learning rates 0.1 and 0.05.
# The accuracy decreased to 72.08% at 0.001, 70.41% at 0.005, and the lowest accuracy was 57.49% at 0.01.
# Conclusion : 
# The results show that the learning rate significantly affects model performance. 
# In this experiment, 0.05 and 0.1 gave the best accuracy (73.33%), while 0.01 performed the worst (57.49%). 
# Therefore, 0.05 or 0.1 can be considered the best learning rate among the tested values for this model.
#
################################################################################
