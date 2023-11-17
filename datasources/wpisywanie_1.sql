use BigBrother 
go

BULK INSERT pracownik
FROM 'C:\!Moje\Studia\sem5\Hurtowania_danych\Zad2\pajton\pracownicy.csv' 
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n' 
);

BULK INSERT stanowisko_kasowe
FROM 'C:\!Moje\Studia\sem5\Hurtowania_danych\Zad2\pajton\kasy.csv' 
WITH
(
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n' 
);

BULK INSERT obsluga
FROM 'C:\!Moje\Studia\sem5\Hurtowania_danych\Zad2\pajton\obsluga.csv' 
WITH
(
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n' 
);

BULK INSERT data
FROM 'C:\!Moje\Studia\sem5\Hurtowania_danych\Zad2\pajton\data.csv' 
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n' 
);

BULK INSERT wniosek
FROM 'C:\!Moje\Studia\sem5\Hurtowania_danych\Zad2\pajton\wniosek.csv'
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n'
);



select * from wniosek;
select * from data;
select * from obsluga;
select * from pracownik;
select * from stanowisko_kasowe;