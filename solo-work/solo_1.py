# zadanie 1.1

hello = "Hello"
student = "Daria"

# oczekiwany rezultat: Hello Ola
komunikat = "{} {}".format(hello, student)
print(komunikat)


# zadanie 1.2

student = input("Wpisz swoje imię: ")
print("Hello " + student)

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

# policz liczbe studentow w tablicy studenci 
# oczekiwany rezultat: Liczba studentow wynosi: 4
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

# oczekiwany rezultat: "Wynik wynosi: 81"
print("Wynik wynosi:", wynik)

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = 0

for znak in ciag_znakow:
    if znak == "(":
        liczba_nawiasow_otwierajacych += 1

# oczekiwany rezultat: "Liczba nawiasow otwierajacych wynosi: 4"
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)



