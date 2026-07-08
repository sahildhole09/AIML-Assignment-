import threading
import time

def Prime(number):
    print("The Prime Numbers are : ")
    for no in number:
        if(no>1):
            for i in range(2,no):
                if(no % i == 0):
                    break
                else:
                    print(no,end="")
    print()

def NonPrime(number):
    print("The NonPrime Numbers are : ")
    for no in number:
        if(no<=1):
            print(no,end="")
        else:
            for i in range(2,no):
                if(no % i == 0):
                    print(no,end="")
    print()

def main():
    n = int(input("Enter total elements : "))

    number = list()

    for i in range(n):
        num =int(input("Enter actual list elements : "))
        number.append(num)

    prime = threading.Thread(target=Prime,args=(number,))
    nonprime = threading.Thread(target=NonPrime,args=(number,))

    prime.start()
    prime.join()

    nonprime.start()
    nonprime.join()

if __name__ == "__main__":
    main()