def Digits(no):
     
     count = 0
     while(no!=0):
         no = no // 10
         count = count + 1
    
     print(f"Number of Digits is : {count}")


def main():
    num = int(input("Enter the number : "))

    Digits(num)

if __name__ == "__main__":
    main()