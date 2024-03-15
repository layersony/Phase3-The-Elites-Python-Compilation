from musicClass import Artist, Song, Genre
import sqlite3

CONN = sqlite3.connect('music.db')
cursor = CONN.cursor()


# create the tables
def tablecreation():
    Artist.createTable(cursor, CONN)
    Song.createTable(cursor, CONN)
    Genre.createTable(cursor, CONN)

def getAllArtist():
    arrayData = Artist.queryAll(cursor, CONN)
    for artist in arrayData:
        print(f'''
    Name: {artist[1]}
    Record Label: {artist[2]}
    ----------------------------
        ''')

def create_artist():
    name = input('Name: ')
    recordlabel = input('Record Label: ')

    artist = Artist(name, recordlabel)
    artist.save(cursor, CONN)

    print('Artist created successfully')

def artistSongs():
    artistname = input('Artist Name: ')

    allSongs = Song.artist_songs(artistname, cursor, CONN)

    for song in allSongs:
        print(f'''
        Song Name: {song[0]}
        Genre: {song[1]}
        ''')

def main():

    selectOption = input('Option >> ')

    if selectOption == '0':
        exit()
    elif selectOption == '1':
        getAllArtist()
    elif selectOption == '2':
        pass 
    elif selectOption == '3':
        pass 
    elif selectOption == '4':
        create_artist() 
    elif selectOption == '5':
        pass 
    elif selectOption == '6':
        pass 
    elif selectOption == '7':
        artistSongs() 
    else:
        print('Invalid Option')

    main()


if __name__ == '__main__':
    # create tables if not created
    tablecreation()

    options = '''
0 - Exit Program
1 - List all Artists
2 - List all Songs
3 - List all Genres
4 - Create a new Artist
5 - Create a new Genre
6 - Create a new Song
7 - Get Artist Songs
'''
    print(options)

    main()









