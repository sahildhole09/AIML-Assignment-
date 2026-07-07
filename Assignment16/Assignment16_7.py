Divisible = lambda Num : Num % 5 == 0 

def main():
    Value = int(input("Enter number : "))

    Ret = Divisible(Value)

    print(Ret)

if __name__ == "__main__":
    main()