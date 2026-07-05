Largest = lambda num1,num2,num3 : num1 if num1 >= num2 and num1 >= num3 else num2 if num2 >= num3 else num3 

def main():
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter second number : "))
    n3 = int(input("Enter third number : "))

    Large = Largest(n1,n2,n3)

    print("Largest number is : ",Large)

if __name__ == "__main__":
    main()