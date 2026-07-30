import psutil
import sys
import datetime

def ProcessScan():
    listprocess = []

    try:
        for proc in psutil.process_iter():
            try:
                info = proc.as_dict(attrs=["pid", "name", "username", "status"])
                info["cpu_percent"] = proc.cpu_percent(None)
                info["memory_percent"] = proc.memory_percent()
                info["start_time"] = datetime.datetime.fromtimestamp(proc.create_time()).strftime("%d-%m-%Y %H:%M:%S")

                listprocess.append(info)

            except (psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess):
                pass

        return listprocess

    except Exception as e:
        print("Error :", e)

def DisplayProcess():
    Border = "-" * 70

    Data = ProcessScan()

    print(Border)
    print("Running Process Information")
    print(Border)

    for info in Data:
        print(f"PID           : {info.get('pid')}")
        print(f"Process Name  : {info.get('name')}")
        print(f"Username      : {info.get('username')}")
        print(f"Status        : {info.get('status')}")
        print(f"CPU Usage     : {info.get('cpu_percent'):.2f}%")
        print(f"Memory Usage  : {info.get('memory_percent'):.2f}%")
        print("Start Time    : %s\n"%info["start_time"])
        print(Border)


def main():

    Border = "-" * 70

    print(Border)
    print("Process Monitoring System")
    print(Border)

    if len(sys.argv) == 1:
        DisplayProcess()

    elif len(sys.argv) == 2:

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script displays information of all running processes.")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage : python ProcInfo.py")

        else:
            print("Invalid option")

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()