import multiprocessing
import time
import os

def CountOdd(No):
    Count = 0
    for i in range(1,No+1):
        if i % 2 != 0:
            Count = Count + 1

    print(f"Process ID : {os.getpid()}")
    print(f"The Input Number is : {No}")
    print(f"Count of Odd Number : {Count}")

def main():
    Data = [1000000,2000000,3000000,4000000]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    pobj.map(CountOdd,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"Time required for execution is : {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()