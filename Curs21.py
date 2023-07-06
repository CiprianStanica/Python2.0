# problema diamant
class A():
    def method(self):
        print("Din A")
class B(A):
    def method(self):
        pass
class C(A):
    def method(self):
        print("Din C")
class D(B,C):
    pass

# o clasa bicicleta care mosteneste o clasas vehicul si o clasa tricicleta

def deplaseaza(vehicul):
    return vehicul.deplaseaza()

class Vehicul():
    def __init__(self):
        self.viteza_maxima = 30
    def deplaseaza(self):
        print("Vehiculul se deplaseaza")

class Tricicleta():
    def __init__(self):
        self.coroane = True
    def deplaseaza(self):
        print("Tricicleta se deplaseaza")

class Bicicleta(Tricicleta,Vehicul):
    pass

# vehicul = Vehicul()
# tricicleta= Tricicleta()

# deplaseaza(vehicul)
# deplaseaza(tricicleta)

# Scrie 2 clase, masina si tir, care sa aiba metoda porneste. Creati o functie care sa apeleaza metoda specifica clasei

class Masina():
    def __init__(self):
        self.porneste = print("Am pornit la drum!")

class Tir():
    def __init__(self):
        self.porneste = print("Tirul a pornit la drum!")

# Creati 3 clase Maina Avion BIcicleta si fiecare dintre ele sa aiba metoda misca()(nu folositi mostenirea)
# o lista numita vehicule care sa contina cate 2 obiecte din fiecare clasa
# parcurcgeti lista si apelati functia misca a fiecarui obiect

class Masina():
    def __init__(self):
        self.misca = print("masina se misca")
class Avion():
    def __init__(self):
        self.misca = print("avionul se misca")
class Bicicleta():
    def __init__(self):
        self.misca = print("bicicleta se misca")

vehicule = []

# O clasa numita persoana cu atributele nume si varsta si o metoda numita salut. Apoi creati clasele student si angajat care mostenesc clasa persoana, apelati metoda saluta pentru fiecare clasa. Suprascrieti apoi metoda din student si rulati, Suprascrieti apoi emtoda din angajat si rulati

        