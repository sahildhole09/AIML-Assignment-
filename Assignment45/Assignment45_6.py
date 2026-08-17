import pandas as pd
import matplotlib.pyplot as plt

def main():
    border = "-"*40

    data = {
        "Name" : ["Amit","Sagar","Pooja"],
        "Math" : [85,90,78],
        "Science" : [92,88,80],
        "English" : [75,85,82]
    }

    df = pd.DataFrame(data)

    print(border)
    print("Dataframe is : ")
    print(border)

    print(df)

    df["Total"] = df[["Math","Science","English"]].sum(axis=1)

    print(border)
    print("Original Dataframe : ")
    print(border)

    print(df)

    print(border)
    print("Dataframe after adding Status column : ")
    print(border)

    df["Status"] = df["Total"].apply(lambda x :"Pass" if x >= 250 else "Fail")

    print(df)
    print(border)

    passed_students = (df["Status"] == "Pass").sum()

    print("Count of Passed Students : ",passed_students)
    print(border)
    
if __name__ == "__main__":
    main()