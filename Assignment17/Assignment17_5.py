def Prime(no):
    if(no <= 1):
        print("It is not Prime Number")
    else:
        for i in range(2,no):
            if no % i == 0:
                print("It is not Prime Number")
                break
        else:
            print("It is Prime Number")

def main():
    num = int(input("Enter number : "))

    Prime(num)

if __name__ == "__main__":
    main()