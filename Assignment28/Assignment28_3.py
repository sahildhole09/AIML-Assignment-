def main():
    try:
        fobj = open("Demo.txt","r")

        for line in fobj:
            print(line,end="")

        fobj.close()

    except FileNotFoundError as flt:
        print("File not Found")

if __name__ == "__main__":
    main()