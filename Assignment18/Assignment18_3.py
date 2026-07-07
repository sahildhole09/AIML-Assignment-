def main():
    n = int(input("Enter the number of elements : "))

    lst = list()

    for i in range(n):
        num = int(input("Enter input elements : "))
        lst.append(num)

    #print(lst)

    min = lst[0]

    for i in lst:
        if(i < min):
            min = i

    print(f"Minimum is : {min}")  

if __name__ == "__main__":
    main()