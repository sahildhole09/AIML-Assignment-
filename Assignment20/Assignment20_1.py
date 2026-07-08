import threading
import time

def EvenNo():
    print("TID of Even Thread is : ",threading.get_ident())
    for i in range(2,21,2):
        print(i)

def OddNo():
    print("TID of Odd Thread is : ",threading.get_ident())
    for i in range(1,20,2):
        print(i)

def main():
    print("TID of Main Thread is : ",threading.get_ident())

    start_time = time.perf_counter()

    Even = threading.Thread(target = EvenNo)
    Odd = threading.Thread(target = OddNo)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

    end_time = time.perf_counter()

    print(f"The time required is : {end_time-start_time:.5f}")

if __name__ == "__main__":
    main()