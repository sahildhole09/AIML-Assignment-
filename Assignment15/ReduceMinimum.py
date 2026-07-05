from functools import reduce
Minimum = lambda x,y : x if x < y else y

def main():
    abc = [45,32,55,68,58]

    min = reduce(Minimum,abc)

    print("Minimum number is : ",min)

if __name__ == "__main__":
    main()