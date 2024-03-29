# zadanie 1.1

hello = "Hello"
student = "Daria"


komunikat = "{} {}".format(hello, student)
print(komunikat)


# zadanie 1.2

student = input("Wpisz swoje imię: ")
print("Hello " + student)

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]


liczba_studentow = len(studenci)
print("Liczba studentów wynosi:", liczba_studentow)

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]
for student in studenci:
    print("Hello", student)

# petla for i w oczekiwanym rezultacie Hello x4 z każdym z osobna 

# zadanie 1.5

liczba = 3
potega = 4

wynik = liczba ** potega


print("Wynik wynosi:", wynik)

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = 0

for znak in ciag_znakow:
    if znak == "(":
        liczba_nawiasow_otwierajacych += 1


print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.8

# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

# split zwraca mi drugi element listy czyli nazwisko
def nazwisko(student):
    return student.split()[-1]

studenci.sort(key=nazwisko)

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie1.9

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
for student in studenci:
    if student.split()[-1][0] == "N":
        liczba_n += 1

print("Liczba studentow na N wynosi:", liczba_n)

# zadanie 1.10

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

def czy_funkcja_liniowa(wykres):
    
    x1, y1 = wykres[0]
    x2, y2 = wykres[1]
    x3, y3 = wykres[2]
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        return True
    else:
        return False

wykres_1_funkcja_liniowa = czy_funkcja_liniowa(wykres_1)
wykres_2_funkcja_liniowa = czy_funkcja_liniowa(wykres_2)
wykres_3_funkcja_liniowa = czy_funkcja_liniowa(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")