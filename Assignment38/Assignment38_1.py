import pandas as pd

Dataset = "student_performance_ml.csv"

df = pd.read_csv(Dataset)

print("Dataset loaded successfully\n")

print("First 5 records : \n",df.head())

print("Last 5 records : \n",df.tail())

print("Total number of rows and columns : \n",df.shape)

print("Column Names : \n",df.columns)

print("Datatypes of each column : \n",df.dtypes)
