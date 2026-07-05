Multiplication = lambda Num1,Num2 : Num1 * Num2

def main():
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter second number : "))
    
    Mult = Multiplication(n1,n2)

    print("Multiplication is : ",Mult)

if __name__ == "__main__":
    main()