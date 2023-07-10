# Create a class called CIrcle that has attributes radius and color. Add methods to calculate the a..
# 1. Create a class called Circle that has attributes radius  and color. Add methods to calculate the area and circumference of the circle
pi = 3.14
class Circle():
    def __init__(self, raza, culoare):
        self.radius = raza
        self.color = culoare
    def arie(self):
        arie = pi*self.radius**2
        return arie
# cerculet = Circle(10,"red")
# print(cerculet.arie())

# 2. Create a class called REctangle that has attributes width and height. Add methods to calculate the area and perimeter of the rectangle


class Patrulater():
    def __init__(self,lungime,latime):
        self.lungime = lungime
        self.latime = latime
    
    def area():
        pass

    def perimetru():
        pass
class Rectangle(Patrulater):
    def __init__(self,lungime,latime):
        super().__init__(lungime,latime)

    # def __init__(self,width,height,lenght):
    #     self.width = width
    #     self.height = height
    #     self.lenght = lenght

    def arie(self):
        arie = self.lungime * self.latime
        return arie
    
    def perimetru(self):
        perimetru = self.lungime*2 + self.latime*2
        return perimetru
    
# dreptunghi = Rectangle(5,5)
# print(dreptunghi.arie())
# print(dreptunghi.perimetru())

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
        
cont_bancar = BankAccount("1234",1000)
print(cont_bancar.adauga_bani(500))
print(cont_bancar.retrage_bani(5000))