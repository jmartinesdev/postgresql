import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the 'Artist' table
# cursor.execute('SELECT * FROM "Artist"')

# query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query 4 - select only by "ArtistID" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# query 5 - select only by "ArtistID" #51 on the "Album" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results
results = cursor.fetchall()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
