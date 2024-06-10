class Game:
    def __init__(self, title):
        self._title = title
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def set_title(self, value):
        if isinstance(value, str) and len(value) > 0 and not hasattr(self, "title"):
            self._title = value
        else:
            return ("no")
        
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return [result.player for result in self.results()]
    
    def average_score(self, player):
        pass
        
class Player:
    def __init__(self, username):
        self._username = username
        
    @property
    def username(self):
        return self._username

    @username.setter
    def set_username(self, value):
        if (type(value, str)) and 2 <= len[value] <= 16:
            self._username = value
        else:
            return ("Username must be string of 2 to 16 characters")
        
    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return [result.game for result in self.results()]

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:
    
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        self.__class__.all.amend(self)
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def set_score(self, value):
        if (type(value, int)) and 1 <= value <= 5000 and not hasattr(self, 'score'):
            self._score = value
        else:
            return ("oh no you don't")
            