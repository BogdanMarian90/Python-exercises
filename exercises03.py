# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# Afișeaz-o.
# Inversează ordinea folosind slicing și suprascrie această listă.
# Printează varianta actuală (inversată).
# Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
# Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

# initializare lista
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
print(note_muzicale)
# inversare prin slicing
note_muzicale = note_muzicale[::-1]
print(f"lista inversata este {note_muzicale}")
note_muzicale.reverse()
print(f"lista initiala este {note_muzicale}")

print("-" * 30)

# 2. De câte ori apare ‘do’?
nr_aparitii = note_muzicale.count("do")
print(f"do apare de {nr_aparitii} ori")

print("-" * 30)

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

# concatenare cu +
varianta1 = lista1 + lista2
print(f"varianta 1 este {varianta1}")

# folosim extend
varianta2 = lista1.copy()
varianta2.extend(lista2)
print(f"varianta 2 este {varianta2}")

# Sau asa
lista1.extend(lista2)
print(f"varianta 3 este {lista1}")

print("-" * 30)

# 4.
# Sortează și afișează lista generată la exercițiul anterior.
# Șterge numărul 0 folosind o funcție.
# Afișaza iar lista.

# Facem sortare la varianta 1
lista1.sort()
print(f"sortam lista1 {lista1}")

print("-" * 30)

# Stergem 0
lista1.pop(2)
print(lista1)

print("-" * 30)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# Lista este goală.
# Lista nu este goală.
lista1 = [3, 1, 0, 2]
if len(lista1) == 0:
    print(f"Lista e goala")
else:
    print(f"Lista nu e goala, lista are {len(lista1)} elemente")

print("-" * 30)

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lista1 = [3, 1, 0, 2]
# Folosim clear
lista1.clear()
print(lista1)

print("-" * 30)

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
# Lista e goala


# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8,
         'Gigel': 10,
         'Dorel': 5
         }
for elev in dict1.keys():
    print(elev)

print("-" * 30)

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
dict1 = {'Ana': 8,
         'Gigel': 10,
         'Dorel': 5
         }
# pentru fiecare  elev = keie, nota = valoarea elev + nota = items
for elev, nota in dict1.items():
    print(f"{elev} a luat nota {nota}")

print("-" * 30)

# 10. Dorel a făcut contestație și a primit 6
# Modifică nota lui Dorel în 6
# Printează nota după modificare
dict1 = {'Ana': 8,
         'Gigel': 10,
         'Dorel': 5
         }
dict1["Dorel"] = 6
print(f"Dorel a luant nota {dict1['Dorel']}")

print("-" * 30)

# 11. Gigel se transferă din clasă
# Căuta o funcție care să îl șteargă
# Vine un coleg nou. Adaugă Ionică, cu nota 9
# Printează noii elevi
dict1 = {'Ana': 8,
         'Gigel': 10,
         'Dorel': 5
         }
del dict1["Gigel"]
dict1["Ionica"] = 9
for elev in dict1.keys():
    print(elev)

print("-" * 30)

# 12. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
#
# Declară o Listă cu 5 jucători
# Schimbari_efectuate = te joci tu cu valori diferite
# Schimbari_max = 3
#
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# Efectuează schimbarea
# Șterge jucătorul scos din listă
# Adaugă jucătorul intrat
# Afișază a intrat x, a ieșit y, mai ai z schimbări
#
# Dacă jucătorul nu e în teren:
# Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
# Afișază ‘mai ai z schimbări’

player_list = ["Messi", "Ronaldo", "Hagi", "Kivu", "Zidane"]
changes = 0
max_changes = 3
if "Messi" in player_list:
    player_list[0] = "Mbape"
    changes += 1
    print(f"I change Messi with Mbape, I have left {max_changes - changes}: changes left")
    print(player_list)
else:
    print(f"Messi is not in the field and I have left {max_changes - changes}: changes left")

print("-"*40)
if "Kivu" in player_list:
    player_list[3] = "Vinicius"
    changes += 1
    print(f"I change Kivu with Vinicius, I have left {max_changes - changes}: changes left")
    print(player_list)
else:
    print(f"Kivu is not in the field and I have left {max_changes - changes}: changes left")

print("-"*40)
if "Griezman" in player_list:
    player_list[4] = "Salah"
    changes += 1
    print(f"I change Griezman with Salah, I have left {max_changes - changes}: changes left")
    print(player_list)
else:
    print(f"Griezman is not in the field and I have left {max_changes - changes}: changes left")

print("-" * 30)

# 13.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# Adaugă în zilele_sapt ‘luni’
# Afișează zile_sapt

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add("luni")
print(zile_sapt)

print("-" * 30)

# 14.Folosește un if și verifică dacă:
# Weekend este un subset al zilelor din săptămânii.
# Weekend nu este un subset al zilelor din săptămânii.
if weekend.issubset(zile_sapt):
    print("weekend e un subset")
else:
    print("weekend nu e subset")

print("-" * 30)

# 15. Afișează diferențele dintre aceste 2 seturi.
diferenta = zile_sapt - weekend
print(diferenta)
diferenta = zile_sapt.difference(weekend)
print(diferenta)

print("-" * 30)

# 16. Afișează intersecția elementelor din aceste 2 seturi.
intersectia = zile_sapt & weekend
print(intersectia)
intersectia = zile_sapt.intersection(weekend)
print(intersectia)
