def main():
    n = int(input("Enter the number : "))

    for i in range(1,n+1):
        if n % i == 0:
            print("Factors are : ",i)

if __name__ == "__main__":
    main()