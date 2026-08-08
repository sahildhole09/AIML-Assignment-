import pandas as pd
import matplotlib.pyplot as plt

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

plt.hist(df["StudyHours"],bins=8)

plt.title("Histogram of StudyHours")

plt.xlabel("Study Hours")
plt.ylabel("No.of Students")

plt.show()

# Observations :-
# The distribution shows that most students study between 4 and 7 hours per day. Very few students study less than 2 hours or more than 8 hours. This means most students have moderate study hours