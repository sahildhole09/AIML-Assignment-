import multiprocessing
import time
import os

def SumEven(No):
    Sum = 0
    for i in range(2,No+1,2):
        Sum = Sum + i

    print(f"Process ID : {os.getpid()}")
    print(f"The Input Number is : {No}")
    print(f"Sum of Even Number : {Sum}")

def main():
    Data = [1000000,2000000,3000000,4000000]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    pobj.map(SumEven,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"Time required for execution is : {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()