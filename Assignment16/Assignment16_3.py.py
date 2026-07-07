def Add(No1,No2):
    Addition = No1 + No2
    return Addition

def main():
    Value1 = int(input("Enter Value1 : "))
    Value2 = int(input("Enter Value2 : "))

    Ret = Add(Value1,Value2)

    print(f"Addition of {Value1} and {Value2} is : {Ret}")

if __name__ == "__main__":
    main()