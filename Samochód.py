class Pojazd:
    def __init__(self, marka, model, rok_produkcji, liczba_kol=4):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.liczba_kol = liczba_kol

    def wyswietl_info(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Rok produkcji: {self.rok_produkcji}, Liczba kół: {self.liczba_kol}")

moj_pojazd = Pojazd("Toyota", "Corolla", 2020)

moj_pojazd.wyswietl_info()
