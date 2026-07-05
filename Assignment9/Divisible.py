def main():
    print("Enter the number: ")
    Num = int(input())

    if Num%3==0 and Num%5==0:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible")

if __name__ == "__main__":
    main()