import schedule
import sys
import time
import os
import datetime

def  DirectoryScan(DirectoryName):
    Ret = False
    
    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no such name")
        return
    
    Ret =  os.path.isdir(DirectoryName)
    if(Ret == False):
        print("There is no such directory")
        return

    LogFileName = "DirectoryCountLog.txt"
    fobj = open(LogFileName,"a")

    fobj.write(f"Directory path : {DirectoryName}\n")

    count = 0
    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            count = count + 1
    fobj.write(f"Number of files : {count}\n")

    fobj.write(f"Date and Time : {datetime.datetime.now()}\n")

    print("Log file created successfully")

def main():
    Border = "-"*40
    print(Border)
    print("Marvellous Automations Script")
    print(Border)
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            schedule.every(5).minutes.do(DirectoryScan,sys.argv[1])

            while(True):
                schedule.run_pending()
                time.sleep(1)
            
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print(" Thank you for using Automations Script ")
    print(Border)
        
if __name__ == "__main__":
    main()