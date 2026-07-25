import schedule
import time

def Display(msg):
    print(msg)

def main():
    message = input("Enter the message : ")
    interval = int(input("Enter the intervals in seconds : "))

    if(interval<=0):
        print("Interval should be grater than zero")
        return

    schedule.every(interval).seconds.do(Display,message)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()