import os
import sys

def FileStringOccurrence(FileName,search):
            fobj = open(FileName,"r")
            count = 0
            for line in fobj:
                words = line.split()

                for w in words:
                    if(w == search):
                        count = count + 1

            fobj.close()
            print(count)

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
            FileStringOccurrence(sys.argv[1],sys.argv[2])
    else:
         print("Invalid No. of arguments")

if __name__ == "__main__":
    main()