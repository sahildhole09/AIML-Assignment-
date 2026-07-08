Multiplication = lambda x,y : x * y

def main():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    Ret = Multiplication(num1,num2)

    print(f"Multiplication of {num1} and {num2} is {Ret}")

if __name__ == "__main__":
    main()