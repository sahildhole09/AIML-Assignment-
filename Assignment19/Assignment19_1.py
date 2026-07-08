Power = lambda x : x ** 2

def main():
    num = int(input("Enter number : "))

    Ret = Power(num)

    print(f"Power of {num} is {Ret}")

if __name__ == "__main__":
    main()