def main():
    try:
        fobj = open("Demo.txt","r")

        count = 0
        for line in fobj:
            count = count + 1

        print("Total lines are : ",count)

        fobj.close()

    except FileNotFoundError as fnt:
        print("File not found")

if __name__ == "__main__":
    main()