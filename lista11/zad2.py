import sqlite3

# utworzenie połączenia z bazą przechowywaną w pamięci RAM
connection = sqlite3.connect("baza_danych.db")
# utworzenie obiektu kursora
cursor = connection.cursor()

#tworzenie tabeli studenci z id, imie, nazwisko
command1 = """CREATE TABLE IF NOT EXISTS
studenci(student_id INTEGER PRIMARY KEY, imie TEXT, nazwisko TEXT)"""
cursor.execute(command1)

#tworzenie tabeli oceny
command2 = """CREATE TABLE IF NOT EXISTS
oceny(student_id INTEGER, ocena FLOAT, FOREIGN KEY(student_id) REFERENCES studenci(student_id))"""
cursor.execute(command2)

#dodawanie rekordów
cursor.execute("INSERT INTO studenci VALUES(0, 'Aniela', 'Adamowicz')")
cursor.execute("INSERT INTO studenci VALUES(1, 'Bartosz', 'Beczkowski')")
cursor.execute("INSERT INTO studenci VALUES(2, 'Cezary', 'Cezarski')")

#dodawanie ocen
cursor.execute("INSERT INTO oceny VALUES(0, 5)")
cursor.execute("INSERT INTO oceny VALUES(0, 4)")
cursor.execute("INSERT INTO oceny VALUES(0, 4.5)")
cursor.execute("INSERT INTO oceny VALUES(1, 3)")
cursor.execute("INSERT INTO oceny VALUES(1, 3.5)")
cursor.execute("INSERT INTO oceny VALUES(2, 4.5)")
cursor.execute("INSERT INTO oceny VALUES(2, 2)")
cursor.execute("INSERT INTO oceny VALUES(2, 5)")

#zapytania
#studenci i oceny
cursor.execute("SELECT studenci.imie, studenci.nazwisko, studenci.student_id, oceny.ocena FROM studenci JOIN oceny ON studenci.student_id = oceny.student_id")
print(cursor.fetchall())
#studenci i oceny>=4
cursor.execute("""SELECT studenci.imie, studenci.nazwisko, studenci.student_id, oceny.ocena 
FROM studenci JOIN oceny ON studenci.student_id = oceny.student_id 
WHERE oceny.ocena >= 4""")
print(cursor.fetchall())
#średnia studenta o indeksie 2
cursor.execute("""SELECT AVG(ocena) FROM oceny WHERE student_id = 2""")
print(cursor.fetchall())
#usuń studenta o indeksie 2
cursor.execute("DELETE FROM studenci WHERE student_id = 2")
cursor.execute("SELECT * FROM studenci")
print(cursor.fetchall())

#usuwanie tabel i koniec programu
#connection.execute("DROP TABLE studenci")
#connection.execute("DROP TABLE oceny")
connection.close()