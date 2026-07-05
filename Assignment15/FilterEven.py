Even = lambda num : num % 2 == 0

def main():

    n = [43,12,45,78,54,35,22]

    even = list(filter(Even,n))

    print("Even No. list is : ",even)

if __name__ == "__main__":
    main()
