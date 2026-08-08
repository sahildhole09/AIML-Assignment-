import pandas as pd

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

print("Dataset loaded successfully\n")

print("Total number of students in the dataset : \n",len(df))

print("Count of Students Passed : \n",(df["FinalResult"] == 1).sum())

print("Count of Students Failed : \n",(df["FinalResult"] == 0).sum())
