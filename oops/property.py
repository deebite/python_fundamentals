class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount > 0: 
            self._balance += amount
        else:
            print("Add more paisa")


a = Account(200)

a.balance = 2000  # set using setter method

print(a.balance)  # called using getter method