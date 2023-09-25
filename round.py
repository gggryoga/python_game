import time
from _thread import *
from .game import Game
from .chat import Chat


class Round(object):
    def __init__(self, word, Player_drawing):
        self.word = word
        self.player_drawing = Player_drawing
        self.player_guessd = []
        self.skips = 0
        self.player_scores = {player = 0 for player in players}
        self.time = 75
        self.chat = Chat(self)
        self.start = time.time()
        start_new_thread(self.time_thread, ())

    def time_thread(self):
        while time.time > 0:
            time.sleep(1)
            self.time -= 1
        self.end_round("Time is up")

    def guess(self, player,wrd):
        correct =  wrd == self.word
        if correct:
                self.player_guessd.append(player)
                # TODO: add score to player


    def player_left(self, player):
        if player in self.player_scores:
            del self.player_scores[player]
        
        if player == self.player_drawing:
            self.end_round("Drawing player leaves")

        if player in self.player_guessd:
            self.player_guessd.remove(player)

    def end_round(self,msg):
        pass