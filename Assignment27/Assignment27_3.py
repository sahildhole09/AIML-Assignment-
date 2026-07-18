class Numbers:

    def __init__(self):
        self.Value = int(input("Enter the Value : "))

    def ChkPrime(self):
        if(self.Value <= 1):
            return False
        for i in range(2,int(self.Value ** 0.5) + 1):
            if(self.Value % i == 0):
                return False
        return True
        
    def ChkPerfect(self):
        sum = 0
        
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                sum = sum + i

        return sum == self.Value
    
    def Factors(self):
        print("Factors : ")
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                print(i,end=" ")
        print()

    def SumFactors(self):
        sum = 0
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                sum = sum + i
        return sum

Obj1 = Numbers()
print("Prime : ",Obj1.ChkPrime())
print("Perfect : ",Obj1.ChkPerfect())
Obj1.Factors()
print("Sum of Factors : ",Obj1.SumFactors())

Obj2 = Numbers()
print("Prime : ",Obj2.ChkPrime())
print("Perfect : ",Obj2.ChkPerfect())
Obj2.Factors()
print("Sum of Factors : ",Obj2.SumFactors())
    