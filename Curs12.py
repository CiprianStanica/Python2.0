# Quiz:
raspunsuri = []
raspunsuri_corecte = []
intrebari = [{"intrebare": "Cum se declara un dictionar?",
                      "raspunsuri": "a.{} b.[] c.()",
                      "corect":"b"
                    },
                    {
                        "intrebare": "Cum se defineste o functie?",
                     "raspunsuri" : "a: def functie:  b.def functie():  c.functie()",
                     "corect": "b"
                    },
                    {
                        "intrebare": "CE returneaza urmatoarea operatie: 2+3*2?",
                     "raspunsuri" : "a: 2:  b.3  c.8",
                     "corect": "c"
                    },
                    {
                        "intrebare": "fiind data lista x = [4,2,1,3], ce va afisa x[4]",
                     "raspunsuri" : "a:3  b.2  c.eroare",
                     "corect": "c"
                    },
                    {
                        "intrebare": "Ce face instructiunea elif?",
                     "raspunsuri" : "a:evitam un else si un if  b.e degeaba  c.nu stiu",
                     "corect": "a"
                    }
                    ]
def afiseaza_intrebare(nr_intrebare):
    print(intrebari[nr_intrebare].get("intrebare"))
    print(intrebari[nr_intrebare].get("raspunsuri"))
    raspuns = input("Introduceti varianta: ")
    raspunsuri.append(raspuns)

def afiseaza_intrebari():
    for intrebare in intrebari:
        print(intrebare["intrebare"])
        print(intrebare["raspunsuri"])
        raspuns = input("Introduceti varianta: ")
        raspunsuri.append(raspuns)
        print("\n")
    return
        
    

# def calculeaza_scor_si_reset():
#     for raspuns in raspunsuri:
#         for i in intrebari:
#             if raspuns == i["corect"]:
#                 raspunsuri_corecte.append(raspuns)           
#     for raspuns_corect in range(len(raspunsuri_corecte) + 1):
#         total_raspunsuri_corecte = 1
#         total_raspunsuri_corecte += raspuns_corect
#     print(f"Scorul tau este de {int(total_raspunsuri_corecte/2)} puncte!")
#     if total_raspunsuri_corecte/2 >3:
#         print(f"Felicitari! Ai fost admis!!!!")
#     else:
#         print("Mai pune mana pe carte !!!")

# SAU

def calculeaza_scor_si_reset():
    scor = 0
    for i in range(len(intrebari)):
        if (raspunsuri[i] == intrebari[i]["corect"]):
            scor += 2
    raspunsuri.clear
    return scor


def urmatoarea_intrebare():
    intrebare_curenta = len(raspunsuri)
    if len(intrebari) <= intrebare_curenta:
        print("Nu mai sunt intrebari!")
    else:
        print(afiseaza_intrebare(intrebare_curenta))

def quiz_meniu():
    print("""
1.Start quiz
2.Next question
3.Show score and reset
4.Exit
    """)
        

    while True:
        optiune = input("Alege optiune: ")
        if optiune.isdigit():
            optiune = int(optiune)
            if optiune not in range(1,5):
                print("Optiunea trebuie sa fie in intervalu 1-4!")
                continue
        else: 
            print("Trebuie sa introduceti o cifra")
            continue
        if optiune == 1 or optiune == 2:
            urmatoarea_intrebare()
        if optiune == 3:
            calculeaza_scor_si_reset()
        if optiune == 4:
            exit()


    # scor = calculeaza_scor_si_reset()
    # if scor < 5:
    #     print("Ati picat examenul!")
    # else:
    #     print("Ati promovat!")
    # print(f"Ati obtinut {scor} puncte!")
    


quiz_meniu()
print(raspunsuri)