def main():
    n = int(input("Enter the number of elements : "))

    lst = list()

    for i in range(n):
        num = int(input("Enter input elements : "))
        lst.append(num)

    #print(lst)

    no = int(input("Enter the element to search : "))  

    freq = 0

    for i in lst:
        if i == no:
            freq = freq + 1

    print("The frequency is : ",freq)

if __name__ == "__main__":
    main()