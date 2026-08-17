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

    sagar = df[df["Name"] == "Sagar"].iloc[0]

    subjects = ["Math","Science","English"]

    marks = [sagar["Math"],sagar["Science"],sagar["English"]]

    plt.figure(figsize=(7,5))

    plt.pie(
        marks,
        labels=subjects,
        startangle=90,
        autopct='%1.1f%%'
    )

    plt.title("Sagar's Subject Marks")
    plt.show()
    
if __name__ == "__main__":
    main()