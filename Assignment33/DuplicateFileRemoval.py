import sys
import os
import re
import time
import datetime
import schedule

import DuplicateModule
import LogModule
import MailModule

###############################################################
# Help
###############################################################

def Help():
    print("""
Duplicate File Removal Automation

Usage:
python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>

Example:
python DuplicateFileRemoval.py D:\\Demo 30 abc@gmail.com
""")

###############################################################
# Usage
###############################################################

def Usage():
    print("""
Usage:
python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>
""")

###############################################################
# Validate Email
###############################################################

def ValidateEmail(Email):

    Pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(Pattern, Email):
        return True

    return False

###############################################################
# Validate Directory
###############################################################

def ValidateDirectory(Path):

    Ret = os.path.isabs(Path)
    if(Ret == False):
        return False

    Ret = os.path.exists(Path)
    if(Ret == False):
        return False

    Ret = os.path.isdir(Path)
    if(Ret == False):
        return False

    return True

###############################################################
# Main Processing
###############################################################

def Process(Directory, ReceiverEmail):

    StartTime = datetime.datetime.now()

    Result = DuplicateModule.DeleteDuplicate(Directory)

    EndTime = datetime.datetime.now()

    LogFile = LogModule.CreateLogFile()

    SenderEmail = "yours@gmail.com"

    AppPassword = "your_16_character_app_password"

    EmailStatus = "Not Sent"

    LogModule.WriteLog(LogFile,StartTime,EndTime,Directory,Result,EmailStatus)

    EmailStatus = MailModule.SendMail(SenderEmail,AppPassword,ReceiverEmail,LogFile,StartTime,EndTime,Directory,Result)

    LogModule.WriteLog(LogFile,StartTime,EndTime,Directory,Result,EmailStatus)

###############################################################
# Main
###############################################################

def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            Help()
            return

        elif(sys.argv[1] == "-u" or sys.argv[1] == "--usage"):
            Usage()
            return

    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        Usage()
        return

    Directory = sys.argv[1]
    Interval = sys.argv[2]
    ReceiverEmail = sys.argv[3]

    Ret =  ValidateDirectory(Directory)
    if(Ret == False):
        print("Invalid Directory")
        return

    Ret = Interval.isdigit()
    if(Ret == False):
        print("Interval should be numeric")
        return

    Interval = int(Interval)

    if(Interval <= 0):
        print("Interval should be greater than zero")
        return

    Ret = ValidateEmail(ReceiverEmail)
    if(Ret == False):
        print("Invalid Email Address")
        return

    print("Duplicate File Removal Automation Started...")

    schedule.every(Interval).minutes.do(Process,Directory,ReceiverEmail)
    print("Automation Started...")

    while(True):
        try:
            schedule.run_pending()
            time.sleep(1)

        except KeyboardInterrupt:
            print("\nAutomation Stopped")
            break

        except Exception as e:
            print("Error :", e)

###############################################################

if __name__ == "__main__":
    main()