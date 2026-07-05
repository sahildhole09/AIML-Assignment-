from functools import reduce

Product = lambda x,y : x * y

def main():
    n = int(input("Enter total elements : "))

    lst = list()

    for i in range(n):
        num = int(input("Enter list numbers : "))
        lst.append(num)

    print(lst)

    prod = reduce(Product,lst)

    print("Product of all elements are : ",prod)

if __name__ == "__main__":
    main()

