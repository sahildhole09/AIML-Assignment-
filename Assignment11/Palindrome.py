def main():
    print("Enter the number : ")
    n = int(input())

    rev = 0
    temp = n

    while(n != 0):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    
    if(rev == temp):
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()


#Using For Loop -

def main():
    print("Enter the number : ")
    n = int(input())

    rev = 0

    for i in range(len(n)-1,-1,-1):
        rev = rev * 10 + n[i]

    if n == rev :
        print("Palindrome")
    else:
        print("Not Palindrome")