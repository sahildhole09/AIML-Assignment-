string = lambda x : len(x) > 5

def main():
    n = int(input("Enter total elements : "))

    lst = list()

    for i in range(n):
        num = input("Enter strings : ")
        lst.append(num)

    print(lst)

    strg = list(filter(string,lst))

    print("The List of String Length Greater than 5 is : ",strg)

if __name__ == "__main__":
    main()

