import schedule
import time

def Task1():
    print("Start your weekly goals")

def Task2():
    print("Review your weekly progress")

def Task3():
    print("Weekly work completed")

def main():
    schedule.every().monday.at("09:00").do(Task1)
    schedule.every().wednesday.at("17:00").do(Task2)
    schedule.every().friday.at("18:00").do(Task3)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()