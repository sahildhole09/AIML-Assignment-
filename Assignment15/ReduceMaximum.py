from functools import reduce
Maximum = lambda x,y : x if x > y else y

def main():
    abc = [45,32,55,68,58]

    max = reduce(Maximum,abc)

    print("Maximum number is : ",max)

if __name__ == "__main__":
    main()