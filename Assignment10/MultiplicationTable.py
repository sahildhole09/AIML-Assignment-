def main():
    print("Enter Number: ")
    Number = int(input())

    i=1
    while(i<=10):
        Mult = Number * i
        i+=1

        print(Mult)

if __name__ == "__main__":
    main()