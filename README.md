# Cepik2.0

Aplikacja została stworzona, aby wyświetlać dane statystyczne pochodzące z API Cepik 2.0, które są bardzo nieczytelne
dla zwykłego użytkownika i aby to ułatwić aplikacja ma sczytywać dane wyświetlane w aplikacji rządowej i przekształcać
je na bardziej czytelne i „poukładane”. Jednakże sczytywanie tychże danych pochłania bardzo dużo czasu, zatem aplikacja
przekształca je na zapytania SQL, a następnie zapisuje w bazie danych, gdzie dostęp do nich jest znacznie ułatwiony,
a przede wszystkim szybszy. Na koniec dane powinny zostać przefiltrowane według żądania użytkownika i wyświetlone w 
czytelny sposób w aplikacji webowej napisanej np. w Django lub PHP, czego tu brakuje. 

Pliki:

ConvertingData.py - zczytuje dane z API Cekpik, przekształca je w zapytania SQL i zapisuje do pliku data.txt;

SavingDataToDB.py - zczytuje dane z pliku "data.txt" i dodaje do bazy danych;

data.txt          - przechowuje dane w postaci zapytań SQL;
