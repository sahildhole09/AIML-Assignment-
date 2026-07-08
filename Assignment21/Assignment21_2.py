import threading
import time 

def Maximum(integers):

    max = integers[0]

    for i in integers:
        if(i > max):
            max = i
    print("Maximum Element : ",max)
    
def Minimum(integers):
    min = integers[0]

    for i in integers:
        if(i < min):
            min = i
    print("Minimum Element : ",min)
    
def main():

    start_time = time.perf_counter()

    n = int(input("Enter total list elements : "))
    integers = list()

    for i in range(1,n+1):
        num=int(input("Enter actual list elements : "))
        integers.append(num)

    Thread1 = threading.Thread(target=Maximum,args=(integers,))
    Thread2 = threading.Thread(target=Minimum,args=(integers,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    end_time = time.perf_counter()

    print(f"The time required : {end_time-start_time}")

if __name__ == "__main__":
    main()