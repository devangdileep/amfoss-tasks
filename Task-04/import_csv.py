import mysql.connector
import csv

def fetch_data():
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
    if r[0]==0:
        with open("movies.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  
            row_num = 2  
            for lines in reader:
                try:
                    values = []
                    for v in lines[:8]:
                        if v == '':
                            values.append(None)
                        else:
                            values.append(v)
                    if values[1] is not None:
                        try:
                            values[1] = int(values[1])
                        except:
                            values[1] = None
                    if values[3] is not None:
                        try:
                            values[3] = float(values[3])
                        except:
                            values[3] = None
                    query = "INSERT INTO movies (Series_Title, Released_Year, Genre, IMDB_Rating, Director, Star1, Star2, Star3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(query, values)
                except Exception as e:
                    print("Row", row_num, "skipped due to error:", e)
                row_num += 1
            mydb.commit()
        print("Data imported from movies.csv")
    else:
        print("Data already present in movies table.")
    cursor.close()
    mydb.close()
