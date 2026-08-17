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

    min_math = df["Math"].min()
    max_math = df["Math"].max()

    df["Math"] = (df["Math"] - min_math) / (max_math - min_math)

    print(border)
    print("Dataframe after min-max scaling of Math column : ")
    print(border)

    print(df)

if __name__ == "__main__":
    main()