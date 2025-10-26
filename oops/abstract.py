from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def payment_method(self):
        print("Available Payment Methods")

class CreditCardPayments(Payment):
    def pay(self, amount):
        return f"Credit card pay: {amount}"
    
    def refund(self, amount):
        return f"Credit card refund: {amount}"

class UPIPayments(Payment):
    def pay(self, amount):
        return f"UIP pay: {amount}"
    
    def refund(self, amount):
        return f"UPI refund: {amount}"

CC = CreditCardPayments()
print(CC.pay(2000))
print(CC.refund(1000))
CC.payment_method()

UPI = UPIPayments()
print(UPI.pay(200))
print(UPI.refund(100))
UPI.payment_method()