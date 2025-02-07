# implement abstract class  for two different bank
from abc import ABC, abstractmethod


class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        "Abstract Method"
        pass


class SBI(Bank):
    def interest(self):
        return "SBI interest rate is 5%"


class HDFC(Bank):
    def interest(self):
        return "HDFC interest rate is 6%"


bank_a = SBI()
bank_b = HDFC()

print(bank_a.bank_info())
print(bank_a.interest())

print(bank_b.bank_info())
print(bank_b.interest())
