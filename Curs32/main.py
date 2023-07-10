from BanckAccount import BankAccount
from Bancomat import Bancomat



def meniu(atm):
    print("""
    1. Creeaza cont
    2. Stergere cont
    3. Depunere numerar
    4. Retragere numerar
    """)
    input_text = input("Selecteaza optiunea: ")
    print(input_text)
    if input_text == "1":
        sold = input("Introdu sold: ")
        atm.creeare_cont(sold)

    if input_text == "2":
        atm.afiseaza_conturi()
        nr_cont = input("Ce cont vrei sa stergi? ")
        atm.stergere_cont(nr_cont)
        atm.afiseaza_conturi()

    if input_text == "3":
        nr_cont_depunere = input("In ce cont vrei sa depui?: ")
        suma_depusa = input("Ce suma vrei sa depui?: ")
        atm.depunere_bani(nr_cont_depunere,suma_depusa)
        atm.afiseaza_conturi()

    if input_text == "4":
        nr_cont_retragere = input("In ce cont vrei sa retragi?: ")
        suma_retrasa = input("Ce suma vrei sa retragi?: ")
        atm.retragere_bani(nr_cont_retragere,suma_retrasa)
        atm.afiseaza_conturi()

atm = Bancomat()
while True:
    meniu(atm)

# atm = Bancomat()
# atm.creeare_cont(100)
# atm.creeare_cont(500)
# atm.afiseaza_conturi()
# atm.stergere_cont("ROBTRLRONCRT10000")
# atm.afiseaza_conturi()