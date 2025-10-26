from abc import ABC,  abstractmethod
class Account(ABC):

    branch_name = "SBI Bank"

    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    def __add__(self, other):
        return self._balance + other._balance

    def __gt__(self, other):
        return self._balance > other._balance

class SavingsAccount(Account):

    def __init__(self, balance):
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposite Amount {amount} to Saving account. So new blance: {self._balance}")
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw Amount {amount} from Saving account, So new blance: {self._balance}")
        else:
            print("OOPS! You can't wothraw because the blace is low")

    def get_balance(self):
        return self._balance

class CurrentAccount(Account):

    def __init__(self, balance):
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposite Amount {amount} to Current account. So new blance: {self._balance}")
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw Amount {amount} from Current account, So new blance: {self._balance}")
        else:
            print("OOPS! You can't wothraw because the blace is low")

    def get_balance(self):
        return self._balance

    
s1 = SavingsAccount(5000)
c1 = CurrentAccount(10000)

s1.deposit(1000)
c1.withdraw(2000)

print("Savings Balance:", s1.get_balance())
print("Current Balance:", c1.get_balance())

print("Total Balance:", s1 + c1)
print("Is Savings > Current?", s1 > c1)

