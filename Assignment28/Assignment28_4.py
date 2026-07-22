def main():
    try:
        fobj1 = open("ABC.txt","r")
        Data = fobj1.read()

        fobj2 = open("Demo.txt","w")
        fobj2.write(Data)
        print("Copied Contents Successfully")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError as flt:
        print("File not found")

if __name__ == "__main__":
    main()