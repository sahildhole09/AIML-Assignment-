import schedule
import os
import time
import datetime
import shutil

source = input("Enter source file path : ")
destination = input("Enter destination directory path : ")

def Backup():
    if(os.path.exists(source)):
        filename = os.path.basename(source)
        name,ext = os.path.splitext(filename)

        newname = name+"_"+datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")+ext

        shutil.copy(source,os.path.join(destination,newname))

        file = open("backup_log.txt","a")
        file.write("Backup completed at "+datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S%p")+"\n")

        file.close()

        print("Backup completed successfully")
    else:
        print("Source file not found")

def main():
    schedule.every().hour.do(Backup)

    while(1):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()