def Pattern(no):
    for i in range(no):
        for j in range(no):
            print(j+1,end="")
        print()

def main():
    n = int(input("Enter number : "))

    Pattern(n)

if __name__ == "__main__":
    main()