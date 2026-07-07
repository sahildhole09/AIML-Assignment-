def Factors(no):

    Sum = 0 

    for i in range(1,no):
        if(no % i == 0):
            Sum = Sum + i
            
    print(f"Sum of Factors o {no} is : {Sum}")

def main():
    num = int(input("Enter the number : "))

    Ret = Factors(num)

if __name__ == "__main__":
    main()