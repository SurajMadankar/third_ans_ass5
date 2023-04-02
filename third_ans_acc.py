class Account:

    def __init__(self,title,balance):
        self.title=title
        self.balance=balance

    def ti(self):
        print(self.title)
    def bal(self):
        print(self.balance)
    

        

class SavingsAccount(Account):

    def __init__(self,title,balance,interstRate):
        super().__init__(title, balance)
        self.interestRate=interstRate
    def int(self):
        print(self.interestRate)
    def all(self):
        print(self.title,self.balance,self.interestRate)

obj=Account("Ashish",5000)
obj.ti()
obj.bal()
obj1=SavingsAccount("Ashish",5000,5)
obj1.int()
obj1.all()

