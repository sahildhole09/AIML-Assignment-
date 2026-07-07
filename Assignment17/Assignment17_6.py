def Pattern(no):
    for i in range(no):
        for j in range(no-i):
            print("*",end="")
        print()  

def main():
    n = int(input("Enter the number : "))

    Pattern(n)

if __name__ == "__main__":
    main()