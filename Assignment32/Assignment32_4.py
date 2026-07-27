import sys
import schedule
import time
import os
import shutil

def FileCopy(Source,Destination):
    Ret = os.path.exists(Source)
    if(Ret == False):
        print("There is no such name")
        return
    
    Ret = os.path.isdir(Source)
    if(Ret == False):
        print(f"There is no such directory : {Source}")
        return
    
    Ret = os.path.exists(Destination)
    if(Ret == False):
        print("There is no such name")
        return
    
    Ret = os.path.isdir(Destination)
    if(Ret == False):
        print(f"There is no such directory : {Destination}")
        return
    
    LogFile = open("CopiedFileLog.txt","a")
    
    for FolderName,SubFolder,FileName in os.walk(Source):
        for fname in FileName:
            if(fname.endswith(".txt")):
                sourcefile = os.path.join(Source,fname)
                destinationfile = os.path.join(Destination,fname)

                try:
                    shutil.copy(sourcefile,destinationfile)
                    LogFile.write(fname + " Copied Successfuly...!\n")
                except:
                    LogFile.write(fname + " Not Copied...!\n")

    LogFile.close()
    print("Copy Completed")

def main():
    Border = "-"*40
    print(Border)
    print("Marvellous Automations Script")
    print(Border)
    if(len(sys.argv) == 3):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            schedule.every(10).minutes.do(FileCopy,sys.argv[1],sys.argv[2])

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