import schedule
import time

def Function():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(Function)

    while(1):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()