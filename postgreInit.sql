-- Upewnij się, że tabeli istnieją, zanim spróbujesz je usunąć
DROP TABLE IF EXISTS obsluga CASCADE;
DROP TABLE IF EXISTS pracownik CASCADE;
DROP TABLE IF EXISTS stanowisko_kasowe CASCADE;
DROP TABLE IF EXISTS wniosek CASCADE;
DROP TABLE IF EXISTS data CASCADE;

-- Tworzenie tabel
CREATE TABLE pracownik (
    id_pracownika_pk serial PRIMARY KEY,
    id_obslugi_fk int,
    data_urodzenia date,
    data_zatrudnienia date
);

CREATE TABLE stanowisko_kasowe (
    id_stanowiska_pk serial PRIMARY KEY,
    id_obslugi_fk int,
    numer_kasy smallint
);

CREATE TABLE data (
    id_daty_pk serial PRIMARY KEY,
    id_wniosku_fk int,
    data_przyjecia_wniosku date,
    czy_wakacje boolean,
    czy_wolne boolean,
    dzien_tygodnia varchar(15) CHECK (dzien_tygodnia IN ('poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela')),
    pora_roku varchar CHECK (pora_roku IN ('wiosna', 'lato', 'jesien', 'zima'))
);

CREATE TABLE wniosek (
    id_wniosku_pk serial PRIMARY KEY,
    id_obslugi_fk int,
    id_daty_fk int,
    typ_wnioskowanego_dokumentu varchar(20) CHECK (typ_wnioskowanego_dokumentu IN ('paszport', 'dowod_osobity', 'prawo_jazdy')),
    stan_wniosku varchar(20) CHECK (stan_wniosku IN ('odrzucony', 'zaakceptowany', 'tworzony', 'oczekuje_na_odbior', 'zakonczony')),
    godzina_pobrania_numerka timestamp,
    godzina_zeskanowania_wniosku_przy_okienku timestamp,
    druga_godzina_zeskanowania timestamp
);

CREATE TABLE obsluga (
    id_obslugi_pk serial PRIMARY KEY,
    id_wniosku_fk int,
    id_pracownika_fk int,
    id_stanowiska_fk int
);

-- Tabele zostały utworzone, teraz możesz wykonywać zapytania SELECT
SELECT * FROM wniosek;
SELECT * FROM data;
SELECT * FROM obsluga;
SELECT * FROM pracownik;
SELECT * FROM stanowisko_kasowe;