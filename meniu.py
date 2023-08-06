# Creati un program care are ca scop un meniu.
# Meniul se va selecta prin introducerea de la tastaura a unui numar intre 1 si 5
# captat intr-o variabila.
# Prezentati prin afisare acest sir de caractere:
# “””
# 1 – Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Sterere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi
# Q - Iesire din program
# “””
# Apoi folosindu-va de o constructie if-elif-else afisati:
# - daca utilizatorul scrie de la tastaura 1 afisati “Afisare lista de cumparaturi”
# - daca utilizatorul scrie de la tastaura 2 afisati “Adugare element”
# - daca utilizatorul scrie de la tastaura 3 afisati “Stergere element”
# - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturi”
# - daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element”
# - daca utilizatorul scrie altceva de la tastaura afisati “Alegerea nu exista.
# Reincercati”
# - daca utilizatorul scrie de la tastaura Q afisati “Iesire din program”
#
# """
# """
# Hint...
# O sa lucrati cu:
# - o lista
# - While true
# - if, elif, else
# - break
# - print
#
# """

lista_cumparaturi = []

lista = input("Introdu ce vrei in lista de cumparaturi prin virgula sau spatiu: ")
elemente_lista = lista.split(",")  # ca sa adaugi mai multe elemente despartite prin virgula
lista_cumparaturi.extend(elemente_lista)

while True:
    print("""
          1 - Afisare lista de cumparaturi
          2 - Adaugare element
          3 - Stergere element
          4 - Sterge lista de cumparaturi
          5 - Cautare in lista de cumparaturi
          Q - Iesire din program
          """)

    optiune = input("Introduceti optiunea: ")
    if optiune not in ["1", "2", "3", "4", "5", "Q", "q"]:  # in cazul in care nu apesi ce trebuie
        print("Nu ai ales optiunea corecta!")

    elif optiune == "1":
        print(lista_cumparaturi)
        mai_departe = input("Continua sau iesi (Enter sau q) ")
        while mai_departe not in ["", "q", "Q"]:  # in cazul in care nu apesi ce trebuie
            print("Ai apsat ceva gresit")
            mai_departe = input("Continua sau iesi (Enter sau q) ")
        if mai_departe == "":
            continue
        elif mai_departe.lower() == "q":
            break

    elif optiune == "2":
        element = input("Adauga un element: ")
        lista_cumparaturi.append(element)
        print(f"Ai adaugat {element} in lista ta de cumparaturi")
        mai_departe = input("Continua sau iesi (Enter sau q) ")
        while mai_departe not in ["", "q", "Q"]:
            print("Ai apsat ceva gresit")
            mai_departe = input("Continua sau iesi (Enter sau q) ")
        if mai_departe == "":
            continue
        elif mai_departe.lower() == "q":
            break

    elif optiune == "3":
        element = input("Eterge un element: ")
        lista_cumparaturi.remove(element)
        print(f"Ai sters {element} din lista ta de cumparaturi")
        mai_departe = input("Continua sau iesi (Enter sau q) ")
        while mai_departe not in ["", "q", "Q"]:
            print("Ai apsat ceva gresit")
            mai_departe = input("Continua sau iesi (Enter sau q) ")
        if mai_departe == "":
            continue
        elif mai_departe.lower() == "q":
            break

    elif optiune == "4":
        lista_cumparaturi.clear()
        mai_departe = input("Continua sau iesi (Enter sau q) ")
        while mai_departe not in ["", "q", "Q"]:
            print("Ai apsat ceva gresit")
            mai_departe = input("Continua sau iesi (Enter sau q) ")
        if mai_departe == "":
            continue
        elif mai_departe.lower() == "q":
            break

    elif optiune == "5":
        element_cautat = input("Cauta in lista: ")
        if element_cautat in lista_cumparaturi:
            print(f"{element_cautat} este in lista")
        else:
            print(f"{element_cautat} nu este in lista")
        mai_departe = input("Continua sau iesi (Enter sau q) ")
        while mai_departe not in ["", "q", "Q"]:
            print("Ai apsat ceva gresit")
            mai_departe = input("Continua sau iesi (Enter sau q) ")
        if mai_departe == "":
            continue
        elif mai_departe.lower() == "q":
            break


    elif optiune.upper() == "Q":
        break


