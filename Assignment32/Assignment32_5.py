import sys
import schedule
import time
import os
import shutil

def DeleteEmptyFiles(DirectoryName):
    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no such name")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print(f"There is no such directory : {DirectoryName}")
        return
    
    LogFile = open("DeletedFileLog.txt","a")
    
    for FolderName,SubFolder,FileName in os.walk(DirectoryName):

        for fname in FileName:
            filepath = os.path.join(FolderName,fname)
            try:
                if(os.path.getsize(filepath) == 0):
                    os.remove(filepath)
                    LogFile.write(filepath +"\n")
            except PermissionError:
                print("Permission denied : ",filepath)

    LogFile.close()
    
    print("Empty Files Deleted Successfully...!")

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
            schedule.every(10).seconds.do(DeleteEmptyFiles,sys.argv[1])

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