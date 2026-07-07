import Arithmetic

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Arithmetic.Addition(Value1,Value2)
    print(f"Addition of {Value1} and {Value2} is : {Ret}")

    Ret = Arithmetic.Subtraction(Value1,Value2)
    print(f"Subtraction of {Value1} and {Value2} is : {Ret}")

    Ret = Arithmetic.Multiplication(Value1,Value2)
    print(f"Multiplication of {Value1} and {Value2} is : {Ret}")

    Ret = Arithmetic.Division(Value1,Value2)
    print(f"Division of {Value1} and {Value2} is : {Ret}")

if __name__ == "__main__":
    main()