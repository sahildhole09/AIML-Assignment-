from functools import reduce

def Prime(no):
    if(no<=1):
        return False
    else:
        for i in range(2,no):
            if(no % i == 0):
                return False
                break
        return True

def Multiply(no):
    no = no * 2
    return no

def Max(x,y):
    if(x > y):
        return x
    else:
        return y

def main():
    n = int(input("Enter the total elements : "))

    Numbers = list()

    for i in range(n):
        num = int(input("Enter input elements : "))
        Numbers.append(num)

    print(Numbers)

    PrimeNo = list(filter(Prime,Numbers))
    print("List after filter : ",PrimeNo)

    Mult = list(map(Multiply,PrimeNo))
    print("List after map : ",Mult)

    Maximum = reduce(Max,Mult)
    print("Output of Reduce : ",Maximum)

if __name__ == "__main__":
    main()