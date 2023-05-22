#1. Find-max
#PSEUDOKOD (zakładamy ze lista nie jest pusta)
#fun sum l 
#   Amount elements ? 
#     (0) max -> none
#     (1) max -> l(0)
#     (>1) max -> dzielimy listę na 2 elementy (pierwszy element listy i resztę czyli pozostałe elemnty listy)
#     szukamy maksikum reszty - > find max(reszta)
#     porównujemy pierwszy element z max reszty 
#       if pierwszy > max_reszta -> return pierwsz
#       else pierwszy < max_reszty - > return max_reszty 

def find_max(lista):
    if not lista:  # Sprawdza, czy lista jest pusta
        return None
    if len(lista) == 1:
        return lista[0]
    else:
        first = lista[0]
        reszta = lista[1:]
        max_reszty = find_max(reszta)
        if max_reszty is None or first > max_reszty:
            return first
        else:
            return max_reszty

# Przykładowe użycie
lista_Darii_max = [15, 32, 6, 39, 17]
max_element = find_max(lista_Darii_max)
print(max_element)

#2. sum_of.list  
#Tworzymy funkcje sum_list, ktora przyjmuję listę jako argment
def sum_list (lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sum_list(lista[1:])
    
lista_Darii = [1, 2, 3, 4, 5]
suma=sum_list(lista_Darii)
print(suma)
#poprzez len(list) sprawdzamy czy lista ma długość 0, czyli czy jest pusta
#jeśli tak, zwracamy 0 ponieważ pusta lista będzie 0 
# jeśli nie, zwracamy sumę pierwszego elementu listy i sume rekurencyjnego wywołania sumy reszty listy 
# później aby sprawdzić definiujemy przykładową listę i printujemy wynik sumy       
#PSEUDOKOD 
# fun sum_list l
#    is l empty ? 
#        (yes) y -> 0
#        (no) n -> l(0) + sum(reszta)
# przykład, mamy liste [1, 2, 3] czyli bierzemy 1 + f[2, 3] -> 2 + f[3] -> 3 + f[]  czyli
#ostatnie działenie odda nam 3, drugie 2 i pierwsze 1 czyli mamy sume 6

#3. n!   3! = 2!*3= 1!*2*3= 1*2*3 = 6 n!=(n-1)!*n 
#4. ciąg F.  (0 1 1 2 3 5 8 ..)
#5*. sudoku 