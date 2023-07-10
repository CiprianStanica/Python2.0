from BanckAccount import BankAccount

class Bancomat():

    conturi = []
    nrCont = 10000

    def creeare_cont(self,balanta):
        nrCont = "ROBTRLRONCRT" + str(self.nrCont)
        bankacc = BankAccount(nrCont,balanta)
        self.conturi.append(bankacc)
        self.nrCont += 1

    def depunere_bani(self,nrCont,suma):
        for cont in self.conturi:
            if cont.account_number == nrCont:
                cont.balance = cont.balance + suma

    def retragere_bani(self,nrCont, suma):
        for cont in self.conturi:
            if cont.account_number == nrCont:
                if suma>cont.balance:
                    print("Fonduri insuficiente")
                else:
                    cont.balance = cont.balance - suma

    def stergere_cont(self,nrCont):
        for cont in self.conturi:
            if cont.account_number == nrCont:
                self.conturi.remove(cont)

    def afiseaza_conturi(self):
        for cont in self.conturi:
            cont.afiseaza_cont()
        
