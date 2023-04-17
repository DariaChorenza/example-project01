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




