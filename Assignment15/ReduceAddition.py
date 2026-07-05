from functools import reduce

Addition = lambda n1,n2 : n1 + n2

def main():
    lst = [34,23,15,74,32]

    add = reduce(Addition,lst)

    print("Addition is : ",add)

if __name__ == "__main__":
    main()