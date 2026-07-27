import schedule
import time

def CreateTextFile():
    timestamp = time.strftime("%d_%m_%Y_%H_%M_%S")
    TextFile = "File_%s.txt" %timestamp

    CurrentDate = time.strftime("%d-%m-%Y")
    CurrentTime = time.strftime("%H:%M:%S%p")

    fobj = open(TextFile,"w")
    
    fobj.write(f"FileName : {TextFile}\n")
    fobj.write(f"Creation Date : {CurrentDate}\n")
    fobj.write(f"Creation Time : {CurrentTime}\n")

    print("New Text File Created Successfully...!")

def main():
    schedule.every(1).minutes.do(CreateTextFile)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()