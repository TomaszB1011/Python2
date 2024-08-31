def dzielenie(x, y):
    try:
        wynik = x / y
        return wynik
    except ZeroDivisionError:
        print("Nie można dzielić przez zero!")
    except  TypeError:
        print("Podane wartości muszą być liczbami.")

liczba1 = input("Podaj pierwszą liczbę: ")
liczba2 = input("Podaj drugą liczbę: ")

wynik_dzielenia = dzielenie(liczba1, liczba2)
print("Wynik dzielenia: ", wynik_dzielenia)