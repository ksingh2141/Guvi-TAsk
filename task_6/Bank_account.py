class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self._balance = balance   # encapsulation

    def deposit(self, amt):
        self._balance += amt
        print("Balance:", self._balance)

    def withdraw(self, amt):
        if amt > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amt
            print("Balance:", self._balance)


# Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, acc_no, balance, rate):
        super().__init__(acc_no, balance)
        self.rate = rate

    def interest(self):
        print("Interest:", self._balance * self.rate / 100)


# Current Account
class CurrentAccount(BankAccount):
    def __init__(self, acc_no, balance, min_bal):
        super().__init__(acc_no, balance)
        self.min_bal = min_bal

    def withdraw(self, amt):
        if self._balance - amt < self.min_bal:
            print("Minimum balance required")
        else:
            self._balance -= amt
            print("Balance:", self._balance)



s = SavingsAccount("S101", 1000, 5)
s.deposit(500)
s.interest()

c = CurrentAccount("C101", 2000, 500)
c.withdraw(1700)