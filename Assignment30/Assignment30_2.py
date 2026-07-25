import schedule
import datetime
import time

def Display():
    CurrentDateTime = datetime.datetime.now()

    print(f"Current Date and Time : {CurrentDateTime}")

def main():
    schedule.every(1).minutes.do(Display)

    while(1):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()