import schedule
import time

def Display():
    print("Namskar...")

def main():
    schedule.every().day.at("09:00").do(Display)

    while(1):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

