class Account:
    def __init__(self, balance):
        self.balance = balance
        
    # Overload + operator to add balances of two accounts
    def __add__(self, other):
        return self.balance + other.balance

    # Overload > operator to compare balances
    def __gt__(self, other):
        return self.balance > other.balance

    # Overload == operator to check if balances are equal
    def __eq__(self, other):
        return self.balance == other.balance

    # Overload str() to print account nicely
    def __str__(self):
        return f"Account balance: {self.balance} Rs"

    # Overload += operator to deposit money
    def __iadd__(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount")
        return self

acc1 = Account(200)

acc2 = Account(500)

print(acc1+acc2)
print(acc1>acc2)
print(acc1==acc2)
print(acc1)

acc1 += 300   #iadd
print(acc1) 