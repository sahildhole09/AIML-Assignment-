import pandas as pd

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

print("Dataset loaded successfully\n")

print("Average StudyHours : ")
print(df["StudyHours"].mean())

print("Average Attendance : ")
print(df["Attendance"].mean())

print("Maximum PreviousScore : ")
print(df["PreviousScore"].max())

print("Minimum SleepHours : ")
print(df["SleepHours"].min())
