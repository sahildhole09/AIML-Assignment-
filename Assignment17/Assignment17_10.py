def Pattern(no):

    addition = 0
    while(no != 0):
        digit = no % 10
        addition = addition + digit
        no = no // 10  

    print(f"Addition of Digits is : {addition}")

def main():
    n = int(input("Enter the number : "))

    Pattern(n)

if __name__ == "__main__":
    main()