import sqlite3 

db_connection = sqlite3.connect('pets_database.db')
db_cursor = db_connection.cursor()

class Cats:
    def __init__(self, name, age, breed, owner_id):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner_id = owner_id

    def save(self): # instance method
        query_stat = f"""
        INSERT INTO cats (name, age, breed, owner_id)
                VALUES ('{self.name}', {self.age}, '{self.breed}', {self.owner_id})
        """
        db_cursor.execute(query_stat)
        db_connection.commit()

# create a cat instance
cat7 = Cats('Leah', 9, 'somalianbreed', 3)
cat7.save()

