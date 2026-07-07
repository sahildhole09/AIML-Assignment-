def main():
    n = int(input("Enter the number of elements : "))

    lst = list()

    for i in range(n):
        num = int(input("Enter input elements : "))
        lst.append(num)

    #print(lst)

    max = lst[0]

    for i in lst:
        if(i > max):
            max = i

    print(f"Maximum is : {max}")  

if __name__ == "__main__":
    main()