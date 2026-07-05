def Addition(Val1,Val2):
    Add = Val1 + Val2
    return Add

def Subtraction(Val1,Val2):
    Sub = Val1 - Val2
    return Sub

def Multiplication(Val1,Val2):
    Mult = Val1 * Val2
    return Mult

def Division(Val1,Val2):
    Div = Val1 / Val2
    return Div

def main():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    Ret = Addition(num1,num2)
    print("Addition is : ",Ret)

    Ret = Subtraction(num1,num2)
    print("Subtraction is : ",Ret)

    Ret = Multiplication(num1,num2)
    print("Multiplication is : ",Ret)

    Ret = Division(num1,num2)
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()