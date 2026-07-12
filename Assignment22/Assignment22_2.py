import multiprocessing
import os

def Factorial(No):

    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i
    
    print(f"The Process ID : {os.getpid()}")
    print(f"Input Number : {No}")
    print(f"Factorial : {Fact}\n")

    return Fact


def main():
    print(f"The Process ID of Main is : {os.getpid()}")

    Input = [10,15,20,25]

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial,Input)

    pobj.close()
    pobj.join()

    print("Factorials are : ")
    print(Result)

if __name__ == "__main__":
    main()