from abc import ABC, abstractmethod

class BankAccount:
    def CheckBalance(self,username):
        self.username = username
        print(f"Hi{username}!!! \nDisplay the balance")
    @abstractmethod
    def deposite(self):
        pass
    @abstractmethod
    def withdraw(sef):
        pass

class CurrentAccount(BankAccount):
    def deposite(self):
        print("Any time deposite")
    def withdraw(sef):
        print("No limits for with draw")
    
class SavingsAccount(BankAccount):
    def deposite(self):
        print("No limt for deposite")
    def withdraw(sef):
        print("limits for with draw")
    
class SalaryAccount(BankAccount):
    def deposite(self):
        print("Once in a month")
    def withdraw(sef):
        print("No limit, charges are applied")
    
class JointAccount(BankAccount):
    def deposite(self):
        print("2 of them can deposite")
    def withdraw(sef):
        print("No limit, both can be withdraw")
    
class pensionAccount(BankAccount):
    def deposite(self):
        print("Once in a month")
    def withdraw(sef):
        print("20K per day")
    
class FixedDipositAccount(BankAccount):
    def deposite(self):
        print("One time deposite")
    def withdraw(sef):
        print("Once at last")
praveen = CurrentAccount()
kumar = SavingsAccount()
mannavaram = SalaryAccount()
sai = JointAccount()
sarath = pensionAccount()
sunil = FixedDipositAccount()

praveen.CheckBalance("praveen")
praveen.deposite()
praveen.withdraw()

kumar.CheckBalance("kumar")
kumar.deposite()
kumar.withdraw()

mannavaram.CheckBalance("mannavaram")
mannavaram.deposite()
mannavaram.withdraw()

sai.CheckBalance("praveen")
sai.deposite()
sai.withdraw()

sarath.CheckBalance("praveen")
sarath.deposite()
sarath.withdraw()

sunil.CheckBalance("praveen")
sunil.deposite()
sunil.withdraw()
