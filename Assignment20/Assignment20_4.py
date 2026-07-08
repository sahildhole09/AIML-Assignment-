import threading 
import time

def Small(st):
    Count = 0
    for ch in st:
        if(ch.islower()):
            Count = Count + 1

    print(f"Thread ID of Small thread : {threading.get_ident()}")
    print(f"Thread Name of Small thread is : {threading.current_thread().name}")
    print(f"The Count of lowercase characters : {Count}")

def Capital(st):
    Count = 0
    for ch in st:
        if(ch.isupper()):
            Count = Count + 1

    print(f"Thread ID of Capital thread : {threading.get_ident()}")
    print(f"Thread Name of Capital thread is : {threading.current_thread().name}")
    print(f"The Count of uppercase characters : {Count}")

def Digits(st):
    Count = 0
    for ch in st:
        if(ch.isdigit()):
            Count = Count + 1

    print(f"Thread ID of Digit thread : {threading.get_ident()}")
    print(f"Thread Name of Digit thread is : {threading.current_thread().name}")
    print(f"The Count of numeric digits : {Count}")

def main():
    print(f"TID of Main Thread is : {threading.get_ident()}")

    start_time = time.perf_counter()

    str = input("Enter the String : ")

    small = threading.Thread(target=Small,args=(str,))
    capital = threading.Thread(target=Capital,args=(str,))
    digits = threading.Thread(target=Digits,args=(str,))

    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()

    end_time = time.perf_counter()

    print(f"The time required : {end_time-start_time}")

if __name__ == "__main__":
    main()
