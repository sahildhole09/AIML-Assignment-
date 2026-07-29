import os
import datetime

###############################################################
# Function : CreateLogDirectory
# Description : Creates Marvellous directory
###############################################################

def CreateLogDirectory():

    DirectoryName = "Marvellous"

    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        os.mkdir(DirectoryName)

    return DirectoryName

###############################################################
# Function : CreateLogFile
# Description : Creates log file with timestamp
###############################################################

def CreateLogFile():

    Directory = CreateLogDirectory()

    TimeStamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    FileName = f"DuplicateRemovalLog_{TimeStamp}.log"

    FilePath = os.path.join(Directory, FileName)

    return FilePath


###############################################################
# Function : WriteLog
# Description : Writes operation details into log file
###############################################################

def WriteLog(LogFile,StartTime,EndTime,Directory,Result,EmailStatus):

    try:

        fobj = open(LogFile, "w")

        fobj.write("=" * 70 + "\n")
        fobj.write("        MARVELLOUS DUPLICATE FILE REMOVAL LOG\n")
        fobj.write("=" * 70 + "\n\n")

        fobj.write(f"Starting Time           : {StartTime}\n")
        fobj.write(f"Completion Time         : {EndTime}\n")
        fobj.write(f"Scanned Directory       : {Directory}\n\n")

        fobj.write(f"Total Files Scanned     : {Result['TotalFiles']}\n")
        fobj.write(f"Duplicate Files Found   : {Result['DuplicateFiles']}\n")
        fobj.write(f"Duplicate Files Deleted : {len(Result['DeletedFiles'])}\n")
        fobj.write(f"Email Status            : {EmailStatus}\n")

        fobj.write("\n")
        fobj.write("=" * 70)
        fobj.write("\nDeleted Files\n")
        fobj.write("=" * 70)
        fobj.write("\n")

        if len(Result["DeletedFiles"]) == 0:
            fobj.write("\nNo duplicate files found.\n")
        else:
            Count = 1

            for File in Result["DeletedFiles"]:
                fobj.write(f"\n{Count}) {File['File']}\n")
                fobj.write(f"Checksum : {File['Checksum']}\n")

                Count += 1

        fobj.write("\n")
        fobj.write("=" * 70)
        fobj.write("\nLog Generated Successfully\n")
        fobj.write("=" * 70)

    except Exception as e:
        print("Unable to create log file :", e)