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
    print("Dataframe after adding Total column : ")
    print(border)
    print(df)
    print(border)

if __name__ == "__main__":
    main()