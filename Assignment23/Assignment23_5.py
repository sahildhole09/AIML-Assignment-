import multiprocessing
import time
import os

def Factorial(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i

    print(f"Process ID : {os.getpid()}")
    print(f"The Input Number is : {No}")
    print(f"Factorial of number : {Fact}")

def main():
    Data = [10,15,20,25]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    pobj.map(Factorial,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(f"Time required for execution is : {end_time - start_time:.5f} seconds")

if __name__ == "__main__":
    main()