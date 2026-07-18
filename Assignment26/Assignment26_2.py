class Circle:
    PI = 3.14
    
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = int(input("Enter the Radius of Circle : "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"Radius of Circle : {self.Radius}")
        print(f"Area of Circle : {self.Area}")
        print(f"Circumference of Circle : {self.Circumference}")

Obj1 = Circle()

Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()
print()

Obj2 = Circle()

Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()
print()

Obj3 = Circle()

Obj3.Accept()
Obj3.CalculateArea()
Obj3.CalculateCircumference()
Obj3.Display()