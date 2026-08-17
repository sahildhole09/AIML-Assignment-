import pandas as pd


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

    df["Gender"] = ["Male","Male","Female"]

    print(border)
    print("Dataframe after adding Gender column : ")
    print(border)

    print(df)

    average_marks = df.groupby("Gender")[["Math","Science","English","Total"]].mean()

    print(border)
    print("Average marks by Gender : ")
    print(border)

    print(average_marks)
    print(border)

if __name__ == "__main__":
    main()