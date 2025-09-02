import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test"
)
cursor = mydb.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS movies(Series_Title VARCHAR(255),Released_Year INT,Genre VARCHAR(255),IMDB_Rating FLOAT,Director VARCHAR(255),Star1 VARCHAR(255),Star2 VARCHAR(255),Star3 VARCHAR(255))")

cursor.execute("SELECT COUNT(*) FROM movies")
r = cursor.fetchone()
if r==0:
    with open('movies.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for lines in reader:
            query = f"INSERT INTO movies (Series_Title, Released_Year, Genre, IMDB_Rating, Director, Star1, Star2, Star3) VALUES ('{lines[0]}', {lines[1]},'{lines[2]}', {lines[3]}, '{lines[4]}', '{lines[5]}', '{lines[6]}', '{lines[7]}')"
            cursor.execute(query)
            mydb.commit()
else:
    print("Data Fetched from movies.csv")


mydb.close()