import schedule
import datetime
import sys
import time

def CreateLogFile():
    Timestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    LogFileName = "MarvellousLog_%s.txt"%(Timestamp)
    LogFileName = LogFileName.replace("-","_")
    LogFileName = LogFileName.replace(":","_")
    LogFileName = LogFileName.replace(" ","_")

    fobj = open(LogFileName,"w")
    fobj.write("Log file created successfully.\n")
    fobj.write(f"Creation Time : {datetime.datetime.now()}")
    fobj.close()

    print("Log file created successfully...")

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
            print("Please use --h or --u for more information")
    else:
        schedule.every(10).minutes.do(CreateLogFile)

        while(True):
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()
    