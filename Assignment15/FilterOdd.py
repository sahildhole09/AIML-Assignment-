Odd = lambda num : num % 2 != 0

def main():

    n = [43,12,45,78,54,35,22]

    odd = list(filter(Odd,n))

    print("Odd list is : ",odd)

if __name__ == "__main__":
    main()
