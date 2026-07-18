class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the Value1 : "))
        self.Value2 = int(input("Enter the Value2 : "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2
    
Obj1 = Arithmetic()

Obj1.Accept()
print(f"Addition : {Obj1.Addition()}")
print(f"Subtraction : {Obj1.Subtraction()}")
print(f"Division : {Obj1.Division()}")
print()

Obj2 = Arithmetic()

Obj2.Accept()
print(f"Addition : {Obj2.Addition()}")
print(f"Subtraction : {Obj2.Subtraction()}")
print(f"Division : {Obj2.Division()}")