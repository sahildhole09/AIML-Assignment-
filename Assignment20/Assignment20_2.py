import threading
import time

def EvenFact(no):

    Sum = 0
    for i in range(1,no+1):
        if no % i == 0 and i % 2 == 0:
            print(i)
            Sum = Sum + i
    
    print(f"Sum of Even Factors : {Sum}")

def OddFact(no):

    Sum = 0
    for i in range(1,no+1):
        if no % i == 0 and i % 2 != 0:
            print(i)
            Sum = Sum + i
    
    print(f"Sum of Odd Factors : {Sum}")

def main():
    print(f"TID of Main Thread is : {threading.get_ident()}")

    start_time = time.perf_counter()

    num = int(input("Enter the number : "))

    EvenFactor = threading.Thread(target=EvenFact,args=(num,))
    OddFactor = threading.Thread(target=OddFact,args=(num,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    end_time = time.perf_counter()

    print(f"Exit from Main {end_time-start_time}")

if __name__ == "__main__":
    main()