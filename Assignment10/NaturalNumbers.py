def main():
    print("Enter Number:")
    Num = int(input())

    i = 1
    sum = 0
    while i <= Num:
        sum = sum + i
        i = i + 1
    print("Sum of natural numbers is:  ",sum)

if __name__ == "__main__":
    main()