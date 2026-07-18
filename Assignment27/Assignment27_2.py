class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(f"Account Holder Name : {self.Name}")
        print(f"Current Balance : {self.Amount}")

    def Deposit(self):
        amt = float(input("Enter amount for deposit : "))
        self.Amount = self.Amount + amt

    def Withdraw(self):
        amt = float(input("Enter amount to withdraw : "))
        if(amt <= self.Amount):
            self.Amount = self.Amount - amt
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

Obj1 = BankAccount("Sahil Dhole",20000)

Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()

print(f"Interest = {Obj1.CalculateInterest()}")
Obj1.Display()
print()

Obj2 = BankAccount("Yash Dhole",35000)

Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()

print(f"Interest = {Obj2.CalculateInterest()}")
Obj2.Display()
print()





    

    