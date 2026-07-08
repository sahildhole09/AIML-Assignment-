import threading
import time 

def Even(no):
    Sum = 0
    for i in no:
        if(i % 2 == 0):
            print("Even No. are : ",i)
            Sum = Sum + i
    
    print("Sum of Even : ",Sum)

def Odd(no):
    Sum = 0
    for i in no:
        if(i % 2 != 0):
            print("Odd No. are : ",i)
            Sum = Sum + i

    print("Sum of Odd : ",Sum)

def main():

    start_time = time.perf_counter()

    n = int(input("Enter total list elements : "))
    integers = list()

    for i in range(1,n+1):
        num=int(input("Enter actual list elements : "))
        integers.append(num)

    EvenList = threading.Thread(target=Even,args=(integers,))
    OddList = threading.Thread(target=Odd,args=(integers,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

    end_time = time.perf_counter()

    print(f"The time required : {end_time-start_time}")

if __name__ == "__main__":
    main()