def main():
    print("Enter the number : ")
    n = int(input())

    sum = 0
    while(n != 0):
        digit = n % 10
        sum = sum + digit
        n = n // 10

    print("Sum of Digits : ",sum) 

if __name__ == "__main__":
    main()

#Using For Loop -

def main():
    print("Enter the number : ")
    n = int(input())

    sum = 0

    for i in range(1,n):
        digit = n % 10
        sum = sum + digit
        n = n // 10

    print("Sum of digits : ",sum)

if __name__ == "__main__":
    main()