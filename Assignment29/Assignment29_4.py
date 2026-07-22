import os
import sys

def FileComparison(FileName1,FileName2):
            fobj1 = open(FileName1,"r")
            Data1 = fobj1.read()

            fobj2 = open(FileName2,"r")
            Data2 = fobj2.read()

            if(Data1 == Data2):
                 print("Success")
            else:
                 print("Failure")

            fobj1.close()
            fobj2.close()

def main():
    Border = "*"*40 
    print(Border)
    print("File Comparison Script")
    print(Border)
    if(len(sys.argv)==3):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:
            FileComparison(sys.argv[1],sys.argv[2])
    else:
         print("Invalid No. of arguments")

if __name__ == "__main__":
    main()