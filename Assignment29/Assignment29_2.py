import os
import sys

def DisplayFileContent(FileName):
            fobj = open(FileName,"r")
            for line in fobj:
                 print(line,end="")

            fobj.close()

def main():
    Border = "*"*40 
    print(Border)
    print("File Content Script")
    print(Border)
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            DisplayFileContent(sys.argv[1])
    else:
         print("Invalid No. of arguments")


if __name__ == "__main__":
    main()