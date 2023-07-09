# Ex.1
# Write a Python program that asks the user for their name and greets them with a personalized message
# def mesaj_personalizat():
#     cere_nume = input("Introdu aici numele tau: ")
#     print(f"Bine ai revenit, {cere_nume}!")
#     return
# mesaj_personalizat()

# Ex.2
# Write a Python function that takes a string as input and counts the number of vowels (a,e,i,o,u) in the string
# def numar_vocale():
#     input_text = input("Scrie aici ceva: ")
#     vocale = ["a","e","i","o","u"]
#     suma_vocale = 0
#     for caracter in input_text:
#         if caracter in vocale:
#             suma_vocale += 1
#     print(suma_vocale)
# numar_vocale()

# Ex.3
# Write a Python program that asks the user for a sentence and prints the sentence in reverse order:
# def inversare_propozitie(input_text):
#     sir = ""
#     # input_text = input("Scrie aici propozitia ta: ")
#     for caracter in range(len(input_text)-1,-1,-1):
#         sir += input_text[caracter]
#     return sir
# inversare_propozitie()

# Ex. 4
# Write  a Python function that takes a string as input add checks if it is a palindrome
# def verifica_palindrom():
#     input_text = input("Scrie aici: ")
#     propozitie_inversata = inversare_propozitie(input_text)
#     if input_text == propozitie_inversata:
#         print("Propozita este palindrom")
#     else:
#         print("Propozitia nu este palindrom")
# verifica_palindrom()

# Ex. 5
# # Write a Python program that asks the user for a sentence and prints the number of words in the sentence
# def numar_cuvinte_in_propozitie():
#     input_text = input("Scrie aici propozita ta: ")
#     print(f"Propozitia are {len[input_text.split(" ")]}")
# numar_cuvinte_in_propozitie()

# Ex. 6
# Write a Python function that takes a string as input and returns a new string with all the vowels removed
# def elimina_vocale():
#     input_text = input("Scrie aici: ")
#     vocale = ["a","e","i","o","u"]
#     for caracter in input_text:
#         if caracter in vocale:
#             continut = input_text.replace(caracter,"")
#     print(continut)
# elimina_vocale()

# Ex.7 
# Write a Python program that asks the user for a sentence and prints the longest word in the sentence
def cel_mai_lung_cuvant_din_propozitie():
    input_text = input("Scrie aici propozitia ta: ").split(" ")
    


cel_mai_lung_cuvant_din_propozitie()

# Ex.8
# Write a Python function that takes a string as input and returns a new string with the first and last character exchanged

# Ex.9

# def functiamea():
#     dictionar = { 
#     "tabel[coloana1]" : "val1",
#     "tabel[coloana2]" : "val2",
#     "tabel[coloana3]" : "val3",
#     "tabel[coloana4]" : "val4",
#     "tabel[coloana5]" : "val5",
#     "tabel[coloana6]" : "val6",
#     "tabel[coloana7]" : "val7",
#     "tabel[coloana8]" : "val8",
#     "tabel[coloana9]" : "val9"
#     }
#     chei = list(dictionar.keys())
#     nume_fisier = chei[0].split("[")[0]
#     with open(nume_fisier + ".csv","w", newline= "") as file:
#         writer = csv.writer(file)
    
    
    


# functiamea()
