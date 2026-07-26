import os
import sys
import schedule
import time
import datetime

def Display(DirectoryName):

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory with name ",DirectoryName)
        return
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("It is not a directory with name ",DirectoryName)

    print("Directory Scanned : ",DirectoryName)

    for FolderName,SubFolder,FileName in os.walk(DirectoryName):

        count = 0
        for fname in FileName:
            count = count + 1
        print("Total files : ",count)

        count = 0
        for subf in SubFolder:
            count = count + 1
        print("Total Subdirectories : ",count)

    print(f"Scan Time : {datetime.datetime.now()}")

def main():
    Display(sys.argv[1])

    schedule.every(1).minutes.do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()