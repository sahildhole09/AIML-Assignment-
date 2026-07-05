def main():
    n = int(input("Enter the number : "))

    binary = ""

    while(n > 0):
        rem = n % 2
        binary = str(rem) + binary
        n = n // 2

    print("Binary equivalent is : ",binary)
         
if __name__ == "__main__":
    main()