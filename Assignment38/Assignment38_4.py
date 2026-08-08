import pandas as pd

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

print("Dataset loaded successfully\n")

print("Distribution of FinalResult are : ",df["FinalResult"].value_counts())

percentage = df["FinalResult"].value_counts(normalize=True)*100

print("Percentage : ",percentage)

# Yes the Dataset is balanced, because the Percentage of label i.e.FinalResult = 100 % between Pass and Fail types.