class Artist:
    def __init__(self, name, recordLabel):
        self.id = None
        self.name = name
        self.recordLabel = recordLabel

    @classmethod
    def createTable(cls, cursor, CONN):
        query = """
        CREATE TABLE IF NOT EXISTS artist(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100),
            recordlabel VARCHAR(150)
        )
        """
        cursor.execute(query)
        CONN.commit()

    def save(self, cursor, CONN):
        query = f"""
            INSERT INTO artist(name, recordlabel)
                        VALUES('{self.name}', '{self.recordLabel}')
        """
        cursor.execute(query)
        CONN.commit()

        self.id = cursor.lastrowid

    @classmethod
    def queryAll(self, cursor, CONN):
        query = '''
        SELECT * FROM artist
        '''
        data = cursor.execute(query)
        return data.fetchall()

class Song:
    def __init__(self, name, genre, artist):
        self.id = None
        self.name = name
        self.genre = genre
        self.artist = artist

    @classmethod
    def createTable(cls, cursor, CONN):
        query = """
        CREATE TABLE IF NOT EXISTS song (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(200),
            genre_id INT,
            artist_id INT
        )
        """
        cursor.execute(query)
        CONN.commit()

    def save(self, cursor, CONN):
        query = f"""
            INSERT INTO song (name, genre_id, artist_id)
                        VALUES('{self.name}', {self.genre}, {self.artist})
        """
        cursor.execute(query)
        CONN.commit()

        self.id = cursor.lastrowid

    @classmethod
    def artist_songs(self, artist, cursor, CONN):
        # get artist id
        query = f'''
            SELECT id FROM artist WHERE name = '{artist}'
        '''
        data = cursor.execute(query)
        artist_id = data.fetchone()[0]
        
        
        secondQuery = f'''
        SELECT song.name, genre.name FROM song
        JOIN genre ON (genre_id = genre.id)
        Where artist_id = {artist_id}
        '''
        data = cursor.execute(secondQuery)
        songs = data.fetchall()
        return songs

class Genre:
    def __init__(self, name):
        self.id = None
        self.name = name

    @classmethod
    def createTable(cls, cursor, CONN):
        query = """
        CREATE TABLE IF NOT EXISTS genre (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(200)
        )
        """
        cursor.execute(query)
        CONN.commit()

    def save(self, cursor, CONN):
        query = f"""
            INSERT INTO genre(name)
                        VALUES('{self.name}')
        """
        cursor.execute(query)
        CONN.commit()

        self.id = cursor.lastrowid