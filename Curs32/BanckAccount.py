class BankAccount():

    suma_cont = 0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def adauga_bani(self, depunere):
        self.balance += depunere
        return self.balance

    def retrage_bani(self, retrage):
        self.balance -= retrage
        if retrage > self.balance:
            print("Nu mai aveti fonduri")
        return self.balance
    
    def afiseaza_cont(self):
        print(self.account_number + " " + str(self.balance))