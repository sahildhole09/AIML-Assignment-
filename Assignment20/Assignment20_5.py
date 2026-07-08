import threading
import time

def Display1():
    print("Numbers from 1 to 50 are : ")
    for i in range(1,51,1):
        print(i)

def Display2():
    print("Numbers reverse from 50 to 1 are : ")
    for i in range(50,0,-1):
        print(i)

def main():
    print(f"Thread ID of Main Thread : {threading.get_ident()}")

    Thread1 = threading.Thread(target=Display1)
    Thread2 = threading.Thread(target=Display2)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()