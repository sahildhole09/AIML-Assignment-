def main():
    try:
        word = "Marvellous"
        fobj = open("Demo.txt","r")
        Data = fobj.read()

        if word in Data:
            print("Word is present")
        else:
            print("Word is not present")

        fobj.close()

    except FileNotFoundError as flt:
        print("File not found")

if __name__ == "__main__":
    main()