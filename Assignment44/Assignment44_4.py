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
    print("Students who scored more than 85 in Science : ")
    print(df[df["Science"]>85])
    print(border)

if __name__ == "__main__":
    main()