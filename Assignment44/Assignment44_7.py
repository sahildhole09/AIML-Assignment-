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
    print("Dataset is : ")
    print(border)

    print(df)

    df["Total"] = df[["Math","Science","English"]].sum(axis=1)

    print(border)
    print("Dataframe after adding Total column : ")
    print(border)
    print(df)
    print(border)

    plt.figure(figsize=(5,3))

    plt.bar(
        df["Name"],
        df["Total"],
        width=0.4,
        edgecolor = "black",
        linewidth = 1,
        alpha = 0.8,
        label = "Total Marks"
    )

    plt.title("Student Names vs Total Marks")
    plt.xlabel("Student Names")
    plt.ylabel("Total Marks")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()