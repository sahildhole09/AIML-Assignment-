def Factorial(No):
    
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i
    return Fact

def main():
    n = int(input("Enter the number : "))

    Ret = Factorial(n)

    print(f"Factorial of {n} is : {Ret}")

if __name__ == "__main__":
    main()
