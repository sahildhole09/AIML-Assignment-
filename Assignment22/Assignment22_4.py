import multiprocessing
import time

def SumPower(No):
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + i ** 5

    return Sum


def main():
    Data = [1000000,2000000,3000000,4000000]

    start_time = time.perf_counter()

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumPower,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is : ",Result)

    print(f"Time required for execution is {end_time-start_time:.5f}")

if __name__ == "__main__":
    main()