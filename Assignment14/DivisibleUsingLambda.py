Divisible = lambda num : num % 5 == 0

def main():
    Num = int(input("Enter the number : "))

    Ans = Divisible(Num)

    print(Ans)

if __name__ == "__main__":
    main()