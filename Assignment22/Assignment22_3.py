import multiprocessing
import os

def IsPrime(No):
    if(No <= 1):
        return False
    else:
        for i in range(2,int(No ** 0.5)+1):
            if(No % i == 0):
                return False
        return True
    
def CountPrime(n):
    count = 0
    for i in range(2,n+1):
        if IsPrime(i):
            count = count + 1
    return count

def main():

    Input = [10000,20000,30000,40000]

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountPrime,Input)

    pobj.close()
    pobj.join()

    print("Count of Prime Numbers are : ")
    for i in range(len(Input)):
        print(f"{Input[i]} = {Result[i]}")

if __name__ == "__main__":
    main()