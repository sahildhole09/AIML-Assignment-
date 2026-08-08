import pandas as pd

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

print("Dataset loaded successfully\n")

print(df.groupby("FinalResult")
[["StudyHours", "Attendance"]].mean())

# Students who study more hours have a high chance of passing.
# Students with higher attendance have a high chance of passing.
# Students with low study hours and poor attendance are high chances of getting fail.
# StudyHours and Attendance have positive impact on FinalResult and also important factors in student performance.b