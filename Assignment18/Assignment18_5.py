import MarvellousNum

def ListPrime(lst):
    Sum = 0

    for i in lst:
        if MarvellousNum.ChkPrime(i):
            Sum = Sum + i

    return Sum

def main():
    n = int(input("Enter the number of elements : "))

    lst = list()

    for i in range(n):
        num = int(input("Enter input elements : "))
        lst.append(num)

    Ret = ListPrime(lst)

    print("Adition of prime numbers : ",Ret)

if __name__ == "__main__":
    main()