from functools import reduce

def Even(no):
    if no %2 == 0:
        return no

def Square(no):
    no = no ** 2
    return no

def Add(x,y):
    Adds = x + y
    return Adds

def main():
    n = int(input("Enter the total elements : "))

    Numbers = list()

    for i in range(n):
        num = int(input("Enter input elements : "))
        Numbers.append(num)

    print(Numbers)

    EvenNo = list(filter(Even,Numbers))
    print("List after filter : ",EvenNo)

    Sq = list(map(Square,EvenNo))
    print("List after map : ",Sq)

    Addition = reduce(Add,Sq)
    print("Output of Reduce : ",Addition)

if __name__ == "__main__":
    main()