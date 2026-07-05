def main():
    n = int(input("Enter number : "))

    sum = 0

    for i in range(1,n):
        if n % i == 0:
            sum = sum + i
    
    if n == sum:
        print("perfect no.")
    else:
        print("Not perfect no.")

if __name__ == "__main__":
    main()
