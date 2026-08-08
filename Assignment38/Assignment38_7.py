import pandas as pd
import matplotlib.pyplot as plt

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

colors = ["red" if x == 0 else "green" for x in df["FinalResult"]]

plt.scatter(df["StudyHours"],df["PreviousScore"],c=colors)

plt.title("StudyHours vs PreviousScore")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.show()