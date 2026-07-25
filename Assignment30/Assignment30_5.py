import schedule
import datetime
import time

def FileContent():
    fobj = open("Marvellous.txt","a")

    CurrentDateTime = datetime.datetime.now()

    fobj.write(f"Task executed at : {CurrentDateTime} PM\n")

    fobj.close()

def main():
    schedule.every(5).minutes.do(FileContent)

    while(1):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()