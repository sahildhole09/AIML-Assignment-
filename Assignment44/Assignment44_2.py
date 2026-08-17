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

    print(border)
    print("Statistical Report of Dataset :")
    print(border)

    print(df.describe())
    print(border)

if __name__ == "__main__":
    main()