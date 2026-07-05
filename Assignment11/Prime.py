def main():
    print("Enter the number : ")
    n = int(input())

    if(n <= 1):
        print("Not Prime...")
    else:
        for i in range(2,n):
            if n % i == 0:
                print("Not Prime...")
                break
        else:
            print("prime")

if __name__ == "__main__":
    main()
