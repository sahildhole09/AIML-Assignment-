def main():
    try:
        fobj = open("Demo.txt","r")

        count = 0
        for line in fobj:
            words = line.split() 
            count = count + len(words)

        print("Total words are : ",count)

        fobj.close()

    except FileNotFoundError as fnt:
        print("File not found")

if __name__ == "__main__":
    main()