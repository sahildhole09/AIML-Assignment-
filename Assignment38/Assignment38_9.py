import pandas as pd
import matplotlib.pyplot as plt

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

plt.scatter(df["AssignmentsCompleted"],df["FinalResult"])

plt.title("Relationship between AssignmentsCompleted and FinalResult")
plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")

plt.show()

# The scatter plot shows that students who complete more assignments generally pass, while students who complete fewer assignments are more likely to fail. 
# This indicates a positive relationship between AssignmentsCompleted and FinalResult.