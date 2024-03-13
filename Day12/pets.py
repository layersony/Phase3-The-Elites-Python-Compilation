import sqlite3 

db_connection = sqlite3.connect('pets_database.db')

db_cursor = db_connection.cursor()

# adding a cat
query_stat = "INSERT INTO cats (name, age, breed, owner_id) VALUES ('Simba', 4, 'kenyan', 1);"

db_cursor.execute(query_stat)

# adding a owner
query_owner_stat = "INSERT INTO owners (name) VALUES ('John');"

db_cursor.execute(query_owner_stat)


db_connection.commit()