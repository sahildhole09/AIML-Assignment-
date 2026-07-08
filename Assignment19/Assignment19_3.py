from functools import reduce

def Function1(no):
    if(no >= 70 and no <= 90):
        return no
    
def Function2(no):
    Ans = no + 10
    return Ans

def Function3(x,y):
    Product = x * y
    return Product

def main():
    n = int(input("Enter the total elements : "))

    Numbers = list()

    for i in range(n):
        num = int(input("Enter input elements : "))
        Numbers.append(num)

    print(Numbers)

    filt = list(filter(Function1,Numbers))
    print("List after filter : ",filt)

    update = list(map(Function2,filt))
    print("List after map : ",update)

    product = reduce(Function3,update)
    print("Output of Reduce : ",product)

if __name__ == "__main__":
    main()