import multiprocessing
import time

def SumSquare(No):

    Sum = 0 
    for i in range(1,No+1):
        Sum = Sum + i**2

    return Sum


def main():
    # n = int(input("Enter total list elements : "))

    # Integers = list()

    # for i in range(n):
    #     num = int(input("Enter actual list elements : "))

    #     Integers.append(num)

    #     print(Integers)
        Integers = [1000000,2000000,3000000,4000000]

        Result = []

        start_time = time.perf_counter()

        pobj = multiprocessing.Pool()

        Result = pobj.map(SumSquare,Integers)

        pobj.close()
        pobj.join()

        end_time = time.perf_counter()

        print("Result is : ")
        print(Result)

        print(f"Time required is : {end_time-start_time:.5f} seconds")

if __name__ == "__main__":
    main()