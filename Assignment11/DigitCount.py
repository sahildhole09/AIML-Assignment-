def main():
    num = int(input("Enter the number : "))

    count = 0

    while(num != 0):
        num = num // 10
        count = count + 1

    print("Number of digits : ",count)

if __name__ == "__main__":
    main()

#Using For Loop -

def main():
    num = int(input("Enter the number : "))

    count = 0

    for i in range(1,num):
        num = num // 10
        count = count + 1

    print("Number of digits : ",count)

if __name__ == "__main__":
    main()