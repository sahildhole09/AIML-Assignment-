import pandas as pd
import matplotlib.pyplot as plt

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

plt.scatter(df["SleepHours"],df["FinalResult"])

plt.title("SleepHours vs FinalResult")
plt.xlabel("Sleep Hours")
plt.ylabel("FinalResult")

plt.show()

# No, sleeping more does not guarantee success. 
# The graph shows that some students who sleep 6–8 hours pass, but there are also students who sleep 6 hours and fail. 
# This means that sleep is important, but FinalResult also depends on other factors such as StudyHours, Attendance, PreviousScore, and AssignmentsCompleted.