use BigBrother
go

BULK INSERT pracownik
FROM 'C:\!Moje\Studia\sem5\Hurtowania_danych\Zad2\pajton\pracownicy2.csv' 
WITH
(
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n' 
);

BULK INSERT stanowisko_kasowe
FROM 'C:\!Moje\Studia\sem5\Hurtowania_danych\Zad2\pajton\kasy2.csv'
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n' 
);

BULK INSERT obsluga
FROM 'C:\!Moje\Studia\sem5\Hurtowania_danych\Zad2\pajton\obsluga2.csv' 
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n'
);

BULK INSERT data
FROM 'C:\!Moje\Studia\sem5\Hurtowania_danych\Zad2\pajton\data2.csv' 
WITH
(
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n'
);

BULK INSERT wniosek
FROM 'C:\!Moje\Studia\sem5\Hurtowania_danych\Zad2\pajton\wniosek2.csv'
WITH
(
    FIRSTROW = 2,
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n'
);

create table wniosekTemp (
	id_wniosku_pk int not null primary key,
	stan_wniosku varchar(20) CHECK (stan_wniosku IN('odrzucony', 'zaakceptowany', 'tworzony', 'oczekuje_na_odbior', 'zakonczony'))
);

BULK INSERT wniosekTemp
FROM 'C:\!Moje\Studia\sem5\Hurtowania_danych\Zad2\pajton\wniosek3.csv' 
WITH
(
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n'
);

merge into wniosek as target
using wniosekTemp as source
on (target.id_wniosku_pk = source.id_wniosku_pk)
when matched then
	update set
		target.stan_wniosku = source.stan_wniosku;

drop table wniosekTemp

select * from wniosek;
select * from data;
select * from obsluga;
select * from pracownik;
select * from stanowisko_kasowe;