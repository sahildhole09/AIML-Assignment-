Maximum = lambda n1,n2 : n1 if n1 > n2 else n2

def main():
    Num1 = int(input("Enter first number : "))
    Num2 = int(input("Enter second number : "))

    Ret = Maximum(Num1,Num2)

    print("Maximum is : ",Ret)

if __name__ == "__main__":
    main()