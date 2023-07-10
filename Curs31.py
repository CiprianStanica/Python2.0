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
    # print(input_text)
    # for cuvant in input_text:
    #     lista_numere_litere_din_cuvant = []
    #     lista_numere_litere_din_cuvant.append(len(cuvant))
    # print(f"Cuvantul {cuvant} are un numar de {max(lista_numere_litere_din_cuvant)} litere, fiind cel mai lung cuvant")
        


# cel_mai_lung_cuvant_din_propozitie()

# Ex.8
# Write a Python function that takes a string as input and returns a new string with the first and last character exchanged
# def inversare_prima_litera_cu_ultima():
#     input_text = input("Scrie cuvantul tau aici: ")
#     if input_text[0] != input_text[len(input_text)]:
    

# inversare_prima_litera_cu_ultima()

# Ex.9
# Write a Python function that asks the user for two numbers and performs division. Handle the ZeroDivisionError to display a custom error message when the second number is zero:
def impartire(a,b):
    if b == 0:
        raise Exception("Incearca un numar diferit de 0, deoarece orice numar impartit la 0 da tot 0")
    return a / b

# print(impartire(6,0))

# # Ex.1
# Write a Python function that takes a list of integers as input and calculates the average of the numbers. Handle the ValueError exception to display a custom error message when the user enters a non-integer value

# Exercise 2:
# Write a Python function that takes a list of integers as input and calculates the average of the numbers. Handle the ValueError exception to display a custom error message when the user enters a non-integer value.

# Exercise 3:
# Write a Python program that reads a file and prints its contents. Handle the FileNotFoundError exception to display a custom error message when the file does not exist.

# Exercise 4:
# Write a Python program that asks the user to enter their age. Handle the TypeError exception to display a custom error message when the user enters a non-numeric value.

# Exercise 5:
# Write a Python function that takes a dictionary as input and prints the value associated with a given key. Handle the KeyError exception to display a custom error message when the key is not found in the dictionary.

# Exercise 6:
# Write a Python program that asks the user to enter a filename and then reads and prints the contents of the file. Handle the IOError exception to display a custom error message when an error occurs while reading the file.

# Exercise 7:
# Write a Python function that takes a list of numbers as input and calculates the product of all the numbers. Handle the OverflowError exception to display a custom error message when the result exceeds the maximum representable value.

# Exercise 8:
# Write a Python program that performs a database query. Handle the ConnectionError exception to display a custom error message when there is a problem connecting to the database.

# Exercise 9:
# Write a Python function that takes a string as input and converts it to an integer. Handle the ValueError exception to display a custom error message when the input string cannot be converted to an integer.

# Exercise 10:
# Write a Python program that asks the user to enter two file names and then copies the contents of one file to another. Handle the PermissionError exception to display a custom error message when there is a problem accessing the files

# Exercise 1:
# Write a Python function that takes a list of integers as input and returns the maximum value in the list.

# Exercise 2:
# Write a Python function that takes a list of strings as input and returns the index of the first occurrence of the string "apple" in the list.

# Exercise 3:
# Write a Python function that takes a list of integers as input and returns the index of the minimum value in the list.

# Exercise 4:
# Write a Python function that takes a list of strings as input and returns a new list containing only the strings that start with the letter "A".

# Exercise 5:
# Write a Python function that takes a list of integers as input and returns the sum of all the even numbers in the list.

# Exercise 6:
# Write a Python function that takes a list of strings as input and returns the number of occurrences of the string "banana" in the list.

# Exercise 7:
# Write a Python function that takes a list of integers as input and returns a new list where each element is multiplied by 2.

# Exercise 8:
# Write a Python function that takes a list of strings as input and returns a new list containing the lengths of each string.

# Exercise 9:
# Write a Python function that takes a list of integers as input and returns the second smallest value in the list.

# Exercise 10:
# Write a Python function that takes a list of strings as input and returns a new list containing only the unique strings (removing duplicates).


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

