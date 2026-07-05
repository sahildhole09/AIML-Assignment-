Even = lambda num : num % 2 == 0

def main():
    Num = int(input("Enter the number : "))

    Ans = Even(Num)

    print(Ans)

if __name__ == "__main__":
    main()