import psutil
import sys
import os
import time
import schedule
from datetime import datetime

def ProcessScan():

    listprocess = []

    for proc in psutil.process_iter():

        try:
            info = proc.as_dict(attrs=["pid","name","username","status"])

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            info["start_time"] = datetime.fromtimestamp(proc.create_time()).strftime("%d-%m-%Y %H:%M:%S")

            listprocess.append(info)

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    return listprocess

def PlatformSurvillance(FolderName):
    Border = "-" * 70

    Ret = False

    Ret = os.path.exists(FolderName)
    if(Ret == False):
        os.mkdir(FolderName)
        print("Directory created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" % timestamp)

    fobj = open(FileName, "w")

    print("Log File Created :", FileName)

    fobj.write(Border + "\n")
    fobj.write("* Platform Surveillance System *\n")
    fobj.write("Log Creation Time : " + timestamp + "\n")
    fobj.write(Border + "\n\n")

    # --------------------------------------------------
    # CPU Information
    # --------------------------------------------------

    fobj.write("* CPU INFORMATION *\n")
    fobj.write(Border + "\n")

    fobj.write("Number of Active CPU Cores : %s\n" %psutil.cpu_count())
    fobj.write("CPU Usage : %.2f %%\n" %psutil.cpu_percent())

    fobj.write(Border + "\n\n")

    # --------------------------------------------------
    # RAM Information
    # --------------------------------------------------

    memory = psutil.virtual_memory()

    fobj.write("* RAM INFORMATION *\n")
    fobj.write(Border + "\n")

    fobj.write("RAM Usage : %s %%\n" %memory.percent)
    fobj.write("Total RAM Available : %s\n" %memory.total)

    fobj.write(Border + "\n\n")

    # --------------------------------------------------
    # Disk Information
    # --------------------------------------------------

    disk = psutil.disk_usage('/')

    fobj.write("* DISK INFORMATION *\n")
    fobj.write(Border + "\n")

    fobj.write("Disk Usage : %s %%\n" %disk.percent)
    fobj.write("Total Disk : %s\n" %(disk.total))

    fobj.write(Border + "\n\n")

    # --------------------------------------------------
    # Network Information
    # --------------------------------------------------

    netobj = psutil.net_io_counters()

    fobj.write("* NETWORK INFORMATION *\n")
    fobj.write(Border + "\n")

    fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_recv / (1024 * 1024)))

    fobj.write(Border + "\n\n")

    # --------------------------------------------------
    # Running Process Information
    # --------------------------------------------------

    fobj.write("* RUNNING PROCESS INFORMATION *\n")
    fobj.write(Border + "\n")

    Data = ProcessScan()

    for info in Data:

        fobj.write("PID : %s\n" %info["pid"])
        fobj.write("Process Name : %s\n" %info["name"])
        fobj.write("User Name : %s\n" %info["username"])
        fobj.write("Status : %s\n" %info["status"])
        fobj.write("Process Start Time : %s\n" %info["start_time"])
        fobj.write("CPU Usage : %.2f %%\n" %info["cpu_percent"])
        fobj.write("Memory Usage : %.2f %%\n" %info["memory_percent"])
        fobj.write(Border + "\n")

    fobj.write("\n")
    fobj.write(Border + "\n")
    fobj.write("End Of Log File\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():
    Border = "-" * 70

    print(Border)
    print("* Automated Platform Surveillance System *")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script performs the following tasks :")
            print("1. Displays CPU Information")
            print("2. Displays RAM Information")
            print("3. Displays Disk Information")
            print("4. Displays Network Information")
            print("5. Displays Running Process Information")
            print("6. Creates a Log File")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage :")
            print(f"python {sys.argv[0]} Folder_Name")

            print("\nExample :")
            print(f"python {sys.argv[0]} ProcessLogs")

        else:
            PlatformSurvillance(sys.argv[1])

            print("\n Automated Platform Surveillance Completed Successfully.")
            print("Log File Generated Successfully.")

    else:
        print("Invalid Number of Arguments")
        print("Use --h for Help")
        print("Use --u for Usage")

    print(Border)
    print("Thank You For Using Automated Platform Surveillance System")
    print(Border)

if __name__ == "__main__":
    main()