import sys
import os
import time
import datetime
import schedule


def FileScan(FileName):
    try:
        Ret = os.path.exists(FileName)

        if(Ret == False):
            print("There is no such name")
            return
    
        Ret = os.path.isfile(FileName)

        if(Ret == False):
            print("There is no such file")
            return
    
        fobj = open(FileName,"r")
        Data = fobj.read()

        if(Data == ""):
            print("File is empty")
        else:
            print(Data)

        fobj.close()

    except PermissionError:
        print("Permission is denied")
    except:
        print("File cannot be opened")

def main():
    Border = "-"*40
    print(Border)
    print("Python Automation Script")
    print(Border)
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as ")
            print("python FileName.py FileName")
            print("FileName should be absolute path")
        else:
            #FileScan(sys.argv[1])

            schedule.every(1).minutes.do(FileScan,sys.argv[1])

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