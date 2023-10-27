import generatory as gen
def main():
    # procent rekordow - jesli ilosc pracownikow wynosi 1000 i np tyle bylo w 1szym czasie zrobione to jak damy na 30 w drugim wywolaniu funkcji to nam doda 300 kolejnych
    gen.wygenerujPracownikow(1,1,'pracownicy')
    gen.wygenerujPracownikow(gen.ilosc_pracownikow+1,0.3,'pracownicy2')

    gen.wygenerujKasy(1, 1, 'kasy')
    gen.wygenerujKasy(gen.ilosc_kas + 1, 0.3, 'kasy2')

    gen.wygenerujObslugi(1,1,'obsluga')
    gen.wygenerujObslugi(gen.ilosc_obslug +1,0.3,'obsluga2')

    # daty generujemy inaczej, jak chcemy zmienic z jakiego zakresu ostatni lat to mozemy to ponizej zmienic
    # gen.ile_lat=
    gen.wygenerujDaty(1, False)
    gen.wygenerujDaty(gen.ile_lat*365 + 1, True)

    gen.wygenerujWnioski(1, 1, 'wniosek', 'data.csv')
    gen.wygenerujWnioski(gen.ilosc_wnioskow + 1, 0.3, 'wniosek2', 'data2.csv')



if __name__ == '__main__':
    gen.wygenerujUpdateWnioskow()
    #main()
