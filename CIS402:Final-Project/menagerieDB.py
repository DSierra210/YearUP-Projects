import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="",        # <--- Enter in your username
    password=""     # <--- Enter in your password
)

cursor = db.cursor()

cursor.execute("DROP DATABASE IF EXISTS menagerie")
cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)
print("\n")

cursor.execute("CREATE DATABASE menagerie")
cursor.execute("USE menagerie")

cursor.execute("CREATE TABLE pets (name VARCHAR(20), owner VARCHAR(20), species VARCHAR (20), sex CHAR(1), birth DATE, "
               "death DATE)")

cursor.execute("DESC pets")
results = cursor.fetchall()

for i in results:
    print(i)

sql = f"INSERT INTO pets VALUES ({'%s, ' * 5}%s)"
val = [
    ("Fluffy", "Harold", "cat", "f", "1993-02-04", None),
    ("Claws", "Gwen", "cat", "m", "1994-03-17", None),
    ("Buffy", "Harold", "dog", "f", "1989-05-13", None),
    ("Fang", "Benny", "dog", "m", "1990-08-27", None),
    ("Bowser", "Diane", "dog", "m", "1979-08-31", "1995-07-29"),
    ("Chirpy", "Gwen", "bird", "f", "1998-09-11", None),
    ("Whistler", "Gwen", "bird", None, "1998-09-11", None),
    ("Slim", "Benny", "snake", "m", "1996-04-29", None)
]
cursor.executemany(sql, val)
db.commit()
print(f"\n{cursor.rowcount} was inserted\n")

cursor.execute("SELECT * FROM pets")
results = cursor.fetchall()

for i in results:
    print(i)
print("\n")

cursor.execute("SELECT * FROM pets WHERE sex ='f'")
results = cursor.fetchall()

print("Where only sex= 'f'")
for i in results:
    print(i)
print("\n")

cursor.execute("SELECT name, birth FROM pets")
results = cursor.fetchall()

print("Only data from name and birth column")
for i in results:
    print(i)
print("\n")

cursor.execute("SELECT owner, Count(*) AS 'number of pets owner has' FROM pets GROUP BY owner")
results = cursor.fetchall()

print("Showing data for number of pets each owner has")
for i in results:
    print(i)
print("\n")

cursor.execute("SELECT name, birth, MONTH(birth) FROM pets")
results = cursor.fetchall()

print("Showing data for columns name, birth, and the date of the month they were born")
for i in results:
    print(i)

cursor.close()
db.close()
