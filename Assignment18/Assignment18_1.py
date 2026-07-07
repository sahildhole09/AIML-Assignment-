def main():
    n = int(input("Enter the number of elements : "))

    lst = list()

    for i in range(n):
        num = int(input("Enter input elements : "))
        lst.append(num)

    #print(lst)

    Sum = 0

    for element in lst:
        Sum = Sum + element

    print("Output : ",Sum)

if __name__ == "__main__":
    main()