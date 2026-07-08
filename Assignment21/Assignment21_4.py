import threading
import time 

sum = 0
product = 1

def Sum(integers):
    global sum
    for i in integers:
        sum = sum + i
    
def Product(integers):
    global product
    product = 1
    for i in integers:
        product = product * i
    
def main():
    global sum,product

    sum = 0
    product = 1

    start_time = time.perf_counter()

    n = int(input("Enter total list elements : "))
    integers = list()

    for i in range(1,n+1):
        num=int(input("Enter actual list elements : "))
        integers.append(num)

    Thread1 = threading.Thread(target=Sum,args=(integers,))
    Thread2 = threading.Thread(target=Product,args=(integers,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    end_time = time.perf_counter()

    print("Sum is : ",sum)
    print("Product is : ",product)

    print(f"The time required : {end_time-start_time}")

if __name__ == "__main__":
    main()