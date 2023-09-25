from .game import Game

class Player(object):
    def __init__(self, ip, name):
        self.score = 0
        self.game = None
        self.ip = ip
        self.name = name

    def update_score(self, x):
        self.score += x

    def guess(self, string):
        pass

    def disconnect(self):
        pass
    
    def get_ip(self):
        return self.ip

    def get_name(self):
        return self.name
    
    def get_score(self):
        return self.score