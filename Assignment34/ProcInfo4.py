import psutil
import sys
import os
import time
import schedule
import datetime
from mail import SendMail

def ProcessScan():

    listprocess = []

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid","name","username","status"])

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["start_time"] = datetime.datetime.fromtimestamp(proc.create_time()).strftime("%d-%m-%Y %H:%M:%S")

            listprocess.append(info)

        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    return listprocess

def PlatformSurvillance(FolderName, EmailID):

    Border = "-" * 70

    Ret = False

    Ret = os.path.exists(FolderName)
    if(Ret == False):
        os.mkdir(FolderName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" % timestamp)

    fobj = open(FileName, "w")

    fobj.write(Border + "\n")
    fobj.write("* Automated Platform Surveillance System *\n")
    fobj.write("Log Created At : " + timestamp + "\n")
    fobj.write(Border + "\n\n")

    # CPU Information

    fobj.write("* CPU INFORMATION *\n")
    fobj.write(Border + "\n")
    fobj.write("Physical Cores : %s\n"% psutil.cpu_count(logical=False))
    fobj.write("Logical Cores : %s\n"% psutil.cpu_count())
    fobj.write("CPU Usage : %.2f %%\n"% psutil.cpu_percent())
    fobj.write(Border + "\n\n")

    # RAM Information

    memory = psutil.virtual_memory()

    fobj.write("* RAM INFORMATION *\n")
    fobj.write(Border + "\n")
    fobj.write("Total RAM : %.2f GB\n"% (memory.total / (1024 ** 3)))
    fobj.write("Available RAM : %.2f GB\n"% (memory.available / (1024 ** 3)))
    fobj.write("Used RAM : %.2f GB\n"% (memory.used / (1024 ** 3)))
    fobj.write("RAM Usage : %.2f %%\n"% memory.percent)
    fobj.write(Border + "\n\n")

    # Disk Information

    disk = psutil.disk_usage('/')

    fobj.write("* DISK INFORMATION *\n")
    fobj.write(Border + "\n")
    fobj.write("Total Disk : %.2f GB\n"% (disk.total / (1024 ** 3)))
    fobj.write("Used Disk : %.2f GB\n"% (disk.used / (1024 ** 3)))
    fobj.write("Free Disk : %.2f GB\n"% (disk.free / (1024 ** 3)))
    fobj.write("Disk Usage : %.2f %%\n"% disk.percent)
    fobj.write(Border + "\n\n")

    # Network Information

    net = psutil.net_io_counters()

    fobj.write("* NETWORK INFORMATION *\n")
    fobj.write(Border + "\n")
    fobj.write("Bytes Sent : %.2f MB\n"% (net.bytes_sent / (1024 * 1024)))
    fobj.write("Bytes Received : %.2f MB\n"% (net.bytes_recv / (1024 * 1024)))
    fobj.write(Border + "\n\n")

    # Running Processes

    fobj.write("* RUNNING PROCESS INFORMATION *\n")
    fobj.write(Border + "\n")

    Data = ProcessScan()

    for info in Data:

        fobj.write("PID : %s\n" % info["pid"])
        fobj.write("Process Name : %s\n" % info["name"])
        fobj.write("User Name : %s\n" % info["username"])
        fobj.write("Status : %s\n" % info["status"])
        fobj.write("Start Time : %s\n" % info["start_time"])
        fobj.write("CPU Usage : %.2f %%\n" % info["cpu_percent"])
        fobj.write("Memory Usage : %.2f %%\n" % info["memory_percent"])
        fobj.write(Border + "\n")

    fobj.write(Border + "\n")
    fobj.write("End Of Log File\n")
    fobj.write(Border + "\n")

    fobj.close()

    print("Log File Created Successfully")

    # Send Mail
    SendMail(FileName, EmailID)

def main():

    Border = "-" * 70

    print(Border)
    print("* Automated Platform Surveillance System *")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script performs the following tasks:")
            print("1. Monitor Running Processes")
            print("2. Generate Log File")
            print("3. Monitor CPU, RAM, Disk and Network")
            print("4. Send Log File through Email")
            print("5. Automatic Scheduling")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name Receiver_Email")
            print("\nExample :")
            print(f"python {sys.argv[0]} 5 Demo abc@gmail.com")

        else:
            print("Invalid Argument")
            print("Use --h for Help")
            print("Use --u for Usage")

    elif(len(sys.argv) == 4):
        try:
            print("Scheduler Started Successfully")
            print("Press CTRL + C to Stop the Automation\n")

            schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance,sys.argv[2],sys.argv[3])

            PlatformSurvillance(sys.argv[2],sys.argv[3])

            while True:
                schedule.run_pending()
                time.sleep(1)

        except KeyboardInterrupt:
            print("\nAutomation Stopped Successfully")

        except Exception as e:
            print("Error :", e)

    else:
        print("Invalid Number of Arguments")
        print("Use --h for Help")
        print("Use --u for Usage")

    print(Border)
    print("Thank You For Using Automated Platform Surveillance System")
    print(Border)

if __name__ == "__main__":
    main()