def main():
    print("Enter the number : ")
    n = int(input())

    Fact = 1

    for i in range(1,n+1):
        Fact = Fact * i
        
    print(Fact)

if __name__ == "__main__":
    main() 