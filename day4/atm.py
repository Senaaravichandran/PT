class hdfc:
    def __init__(self, balance, amountCrt, amountDebt, cardno):
        self.balance=balance
        self.amountCrt=amountCrt
        self.amountDebt=amountDebt
        self.cardno=cardno
class amountadded(hdfc):
    def add(self):
        self.balance=self.balance+self.amountCrt
        print("Hii",self.balance)
class amountdebited(hdfc):
    def debit(self):
        self.balance=self.balance-self.amountDebt
        print("Hii",self.balance)
        