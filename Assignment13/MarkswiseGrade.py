def main():
    marks = int(input("Enter the marks : "))

    if (marks >= 75):
        print("Distinction")
    elif(marks >= 60):
        print("First Class")
    elif(marks >= 50):
        print("Second Class")
    else:
        print("Fail")

if __name__ == "__main__":
    main()