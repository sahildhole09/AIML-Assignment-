def ChkNum(number):
    if(number % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    Value = int(input("Enter the number : "))

    ChkNum(Value)

if __name__ == "__main__":
    main()