import os
import sys

def CopyFileContent(FileName1):
            fobj1 = open(FileName1,"r")
            Data = fobj1.read()

            fobj2 = open("Demo.txt","w")
            fobj2.write(Data)

            fobj1.close()
            fobj2.close()

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
            CopyFileContent(sys.argv[1])
            print("File Content get copied...")
    else:
         print("Invalid No. of arguments")

if __name__ == "__main__":
    main()