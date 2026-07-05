Square = lambda a : a * a 

def main():
    n = [10,12,4,13]

    Sq = list(map(Square,n))

    print("Square is : ",Sq)

if __name__ == "__main__":
    main()