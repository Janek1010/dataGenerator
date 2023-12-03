import generatory as gen
def main():
    # procent rekordow - jesli ilosc pracownikow wynosi 1000 i np tyle bylo w 1szym czasie zrobione to jak damy na 30 w drugim wywolaniu funkcji to nam doda 300 kolejnych
    gen.wygenerujPracownikowAll()
    gen.wygenerujPracownikow('pracownicyExcel.csv', 'pracownicyBILL.csv')
    gen.wygenerujPracownikow('pracownicyExcel2.csv', 'pracownicy2BILL.csv')

    gen.wygenerujKasy(1, 1, 'kasy')
    gen.wygenerujKasy(gen.ilosc_kas + 1, 0.3, 'kasy2')

    gen.wygenerujObslugi(1,1,'obsluga')
    gen.wygenerujObslugi(gen.ilosc_obslug +1,0.3,'obsluga2')

    gen.wygenerujDaty(1, False)
    gen.wygenerujDaty(gen.ile_lat*365 + 1, True)

    gen.wygenerujWnioski(1, 1, 'wniosek', 'data.csv')
    gen.wygenerujWnioski(gen.ilosc_wnioskow + 1, 0.3, 'wniosek2', 'data2.csv')

    gen.wygenerujUpdateWnioskow()


if __name__ == '__main__':
    main()
