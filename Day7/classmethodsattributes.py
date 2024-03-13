class Games:

    GAME_GENRE = ['Action', 'OpenWorld', 'FPS', 'Sport']
    # class attribute
    no_of_games = 0 #(attribute)

    ALL = []

    def __init__(self, gname, release_year, type):
        if type not in Games.GAME_GENRE:
            print('Type not supported')
        else:
            self.gname = gname
            self.release_year = release_year
            self.type = type

            self.increase_games()

            Games.add_game(self)

            print('Game supported')

    @classmethod # method
    def increase_games(cls):
        cls.no_of_games += 1

    def __str__(self):
        f'{self.gname}'

    @classmethod
    def add_game(cls, game):
        
        cls.ALL.append(game)

    @classmethod
    def view_games(cls):
        return [game.gname for game in cls.ALL]

game1 = Games('COD', '2022', 'Action') # instance of Games
game2 = Games('Fortnite', '2023', 'OpenWorld')
game3 = Games('EAFC', '2024', 'Sport')
game4 = Games('Truth or Dare', '2002', 'Acrade')
game5 = Games('Apex', '2003', 'FPS')

print( Games.view_games() )