# Parametrii

def inmultire(primul_numar:int,al_doilea_numar = 14):
    ''' Aceasta functie inmulteste doua numere
    :param int primul numar: primul numar care se inmulteste
    :param int al doilea numar: al doilea numar care se inmulteste. Daca nu este specificata o valoare, numarul va fi automat 14
    '''
    return primul_numar * al_doilea_numar
inmultire(2,3)
print(inmultire.__doc__)