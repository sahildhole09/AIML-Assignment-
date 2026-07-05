def main():
    n = int(input("Enter number : "))

    rev = 0

    while(n != 0):
        digit = n % 10
        rev = rev * 10 + digit 
        n = n // 10

    print("Reversed number : ",rev)
if __name__ == "__main__":
    main()

#Using For Loop -

def main():
    n = int(input("Enter number : "))

    rev = 0

    for i in range(n):
        digit = n % 10
        rev = rev * 10 + digit 
        n = n // 10
        
    print("Reverse is : ",rev)

if __name__ == "__main__":
    main()