import random
 
class Account:
    # Construct an Account object
    def __init__(self, id, balance = 0, annualInterestRate = 3.4):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate
 
    def getId(self):
        return self.id
 
    def getBalance(self):
        return self.balance
 
    def getAnnualInterestRate(self):
        return self.annualInterestRate
 
    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12
 
    def getwithdraw(self, amount):
        self.balance=self.balance-amount
 
    def getdeposit(self, amount):
        self.balance=self.balance+amount
 
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()
tina = Account (1)
print(tina.getBalance())

print(tina.getdeposit(12000))

print(tina.getBalance())

print(tina.getwithdraw(5000))

print (tina.getBalance())

