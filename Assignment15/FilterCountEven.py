CountEven = lambda x : x % 2 == 0

def main():
    n = int(input("Enter total elements : "))

    lst = list()

    for i in range(n):
        num = int(input("Enter list numbers : "))
        lst.append(num)

    print(lst)

    count = list(filter(CountEven,lst))

    print("The count of Even numbers is : ",len(count))

if __name__ == "__main__":
    main()

