def ChkGreater():
    Num1 = int(input("Enter first number: "))
    Num2 = int(input("Enter second number: "))

    if Num1>Num2:
        print("Greater Number is: ",Num1)
    else:
        print("Greater Number is: ",Num2)

def main():
    ChkGreater()

if __name__ == "__main__":
    main()