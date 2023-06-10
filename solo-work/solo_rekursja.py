#1. Find-max
#PSEUDOKOD (zakładamy ze lista nie jest pusta)
#fun find_max l 
#   Amount elements ? 
#     (0) max -> none
#     (1) max -> l(0)
#     (>1) max -> dzielimy listę na 2 elementy (pierwszy element listy i resztę czyli pozostałe elemnty listy)
#     szukamy maksikum reszty - > find max(reszta)
#     porównujemy pierwszy element z max reszty 
#       if pierwszy > max_reszta -> return pierwsz
#       else pierwszy < max_reszty - > return max_reszty 

def find_max(lista):
    if not lista:  # Sprawdza, czy lista jest pusta, jeżeli tak zwracamy none 
        return None
    if len(lista) == 1:  # Sprawdzamy, czy lista ma 1 element
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
print(f"Maksymalna wartośc w liście {lista_Darii_max} to:", max_element)

print("----------------------------------------")
#2. sum_of.list  
#PSEUDOKOD
# fun sum_list l
#    is l empty ? 
#        (yes) y -> 0
#        (no) n -> l(0) + sum(reszta)
#Tworzymy funkcje sum_list, ktora przyjmuję listę jako argment

def sum_list (lista):
    if len(lista) == 0:     #poprzez len(list) sprawdzamy czy lista ma długość 0, czyli czy jest pusta
        return 0            #jeśli tak, zwracamy 0 ponieważ pusta lista będzie 0 
    else:
        return lista[0] + sum_list(lista[1:])    # jeśli nie, zwracamy sumę pierwszego elementu listy i sume rekurencyjnego wywołania sumy reszty listy

#Przykładowe użycie   
lista_Darii = [1, 2, 3, 4, 5]
suma = sum_list(lista_Darii)
print(f"Suma listy {lista_Darii} wynosi:", suma)
print("----------------------------------------")

#3. Silnia 
#PSEUDOKOD
# fun silnia(n)
#   n = 0?            
#     (yes) y -> 1 (ponieważ 0!=1)
#     (no)  y -> n * silnia(n-1)

def silnia(n):
    if n == 0:           #sprawdzamy czy n równe 0
        return 1
    else:
        return n * silnia(n-1)      #wywołanie rekurencyjnie silni, obliczając silnię dla n-1 i mnożąc ją przez n

# Przykładowe użycie
liczba = 5
wynik = silnia(liczba)
print(f"Silnia z {liczba} wynosi:", wynik)
print("----------------------------------------")

#4 Ciąg fibonaciego
#PSEUDOKOD
# fun fibonacci(n)
#   n <=1 ?         
#     (yes) y -> n        
#     (no)  y -> fibonacci(n-1) + fibonacci(n-2)       

def fibonacci(n):
    if n <= 1:               #sprawdzamy czy n jest mniejsze lub równe 1 
        return n             #pierwsze dwa elementy ciągu Fibonacciego to 0 i 1 dlatego zwracmy n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)       #obliczamy sumę dwóch poprzednich elementów ciągu Fibonacciego (czyli n-1 i n-2).

# Przykładowe użycie
liczba = 6
wynik = fibonacci(liczba)
print(f"Wartość {liczba}-tego elementu ciągu Fibonacciego wynosi:", wynik)
print("----------------------------------------")

#5. sudoku 4x4
#PSEUDOKOD
# fun sudoku(tablica, wiersze, kolumny, wartość)
# dla i od 0 do 3 w wierszu:
#   jeżeli board[row][i] = num               sprawdzamy czy 'num' jest już obecne w danym wierszu
#     jeżeli nie zwróć fałsz 
# dla i od 0 do 3 w kolumnie
#   jeżeli board[i][col] = num               sprawdzamy czy 'num' jest już obecne w danej kolumnie
#     jeżeli nie zwróć fałsz

#sprawdzamy czy 'num' jest poprawną wartością dla podkwadratu 2x2
# start_row = row - row % 2
# start_col = col - col % 2
#    dla i od 0 do 1
#      dla j od 0 so 1
#sprawdzamy czy 'num' jest już obecne w podkwadracie 2x2
#         jeżeli board[start_row + i][start_col + j] == num:
#            jeżeli nie zwróć fałsz 

#wywołanie rekurencyjnej funkcji rozwiązującej sudoku 
# fun solve_sudoku(tablica)
#     dla row od 0 do 3:
#     dla col od 0 do 3:
# sprawdzamy czy komórka jest pusta (wartość 0)
#jeżeli board[row][col] == 0:
#dla num od 1 do 4:
# sprawdzamy czy wartość 'num' jest poprawna dla komórki
#jeżeli sudoku(board, row, col, num):
# przypisujemy wartość 'num' do komórki
#board[row][col] = num
# rekurencyjnie próbujemy rozwiązać Sudoku dla aktualnej planszy
#jeżeli solve_sudoku(board):
# zwróć wynik 

# Jeśli Sudoku nie zostało rozwiązane, przywraca wartość 0 do komórki
#board[row][col] = 0

# Jeśli żadna wartość nie jest poprawna dla komórki, zwraca FAŁSZ
# Jeśli udało się przypisać wartości do wszystkich komórek, Sudoku jest rozwiązane
#zwróć całe rozwiązanie


def sudoku(board, row, col, num):
    # Sprawdza czy 'num' jest poprawną wartością dla danego wiersza
    for i in range(4):
        if board[row][i] == num:
            return False

    # Sprawdza czy 'num' jest poprawną wartością dla danej kolumny
    for i in range(4):
        if board[i][col] == num:
            return False

    # Sprawdza czy 'num' jest poprawną wartością dla podkwadratu 2x2
    start_row = row - row % 2
    start_col = col - col % 2
    for i in range(2):
        for j in range(2):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                for num in range(1, 5):
                    if sudoku(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


# Przykładowa plansza Sudoku 4x4
sudoku_board = [
    [0, 2, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 4],
    [4, 0, 0, 0]
]

if solve_sudoku(sudoku_board):
    print("Rozwiązane Sudoku:")
    for row in sudoku_board:
        print(row)
else:
    print("Nie można rozwiązać Sudoku dla danej planszy.")
print("----------------------------------------")

#5b. sudoku 9x9 
# Do rozwiązania sudoku o wymiarach 9x9 wykorzystałam dokładnie ten sam kod co w przypadku 4x4 
# Zmiany jakie zostały dokonane to długości kolumn, wierszy i wymiarów kwadratów, bo teraz:
#kolumna ma 9 elementów, wiersz 9, a kwadrat jest 3x3 
def sudoku(board, row, col, num):
    # Sprawdza czy 'num' jest poprawną wartością dla danego wiersza
    for i in range(9):
        if board[row][i] == num:
            return False

    # Sprawdza czy 'num' jest poprawną wartością dla danej kolumny
    for i in range(9):
        if board[i][col] == num:
            return False

    # Sprawdza czy 'num' jest poprawną wartością dla podkwadratu 3x3
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if sudoku(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


# Przykładowa plansza Sudoku 9x9
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Rozwiązane Sudoku:")
    for row in sudoku_board:
        print(row)
else:
    print("Nie można rozwiązać Sudoku dla danej planszy.")
