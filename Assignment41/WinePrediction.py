import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Loading Dataset

Dataset = "WinePredictor.csv"

df = pd.read_csv(Dataset)

print("Dataset gets loaded successfully")

# Data Analysis (EDA)

print("Shape of Dataset : ",df.shape)

print("List of Column Names in Dataset : ",df.columns)

print("Missing values per Column : ",df.isnull().sum())

print("Class distribution (Class Count) : ",df["Class"].value_counts())

print("Statistical Report of Dataset",df.describe)

# Independent & Dependent Variable

features = [
    "Alcohol",
    "Malic acid",
    "Ash",
    "Alcalinity of ash",
    "Magnesium",
    "Total phenols",
    "Flavanoids",
    "Nonflavanoid phenols",
    "Proanthocyanins",
    "Color intensity",
    "Hue",
    "OD280/OD315 of diluted wines",
    "Proline"
]

X = df[features]
Y = df["Class"]

print("Shape of Independent Variables : ",X.shape)
print("Shape of Dependent Variables : ",Y.shape)

# Splitting Dataset for training & testing 

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("Training Data : ",X_train.shape)
print("Testing Data : ",X_test.shape)

# Build a model

model = DecisionTreeClassifier(random_state=42)

# Train Data

model.fit(X_train,Y_train)
print("\nTraining Completed...")

# Test Data

Y_pred = model.predict(X_test)

print("\nActual Values : ",Y_test)
print("\nPredicted Values : ",Y_pred)

# Calculate Accuracy

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of Testing Data : ",accuracy*100,"%")