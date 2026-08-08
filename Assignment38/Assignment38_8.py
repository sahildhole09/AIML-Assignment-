import pandas as pd
import matplotlib.pyplot as plt

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

plt.boxplot(df["Attendance"])

plt.title("Attendance BoxPlot")
plt.ylabel("Attendance")

plt.show()

# No outliers are present in the Attendance boxplot. 
# All attendance values fall within the normal range.