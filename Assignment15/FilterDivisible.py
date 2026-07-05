Divisible = lambda x : x % 3 == 0 and x % 5 == 0

def main():
    n = int(input("Enter total elements : "))

    lst = list()

    for i in range(n):
        num = int(input("Enter list numbers : "))
        lst.append(num)

    print(lst)

    div = list(filter(Divisible,lst))

    print("Divisible by 3 and 5 are : ",div)

if __name__ == "__main__":
    main()

