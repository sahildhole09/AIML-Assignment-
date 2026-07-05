def CircleArea(Radius,PI = 3.14):
    Area = PI * Radius * Radius
    return Area

def main():
    r = int(input("Enter the radius : "))

    Ret = CircleArea(r)

    print("Area of Circle : ",Ret)
    
if __name__ == "__main__":
    main()