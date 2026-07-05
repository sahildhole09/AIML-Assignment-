def main():
    print("Enter one number: ")
    n = int(input())

    i=1

    while i <= n:
        if i%2 != 0:
            print(i)
        i = i + 1

if __name__ == "__main__":
    main()