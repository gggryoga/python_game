from .player import Player
from .board import Board
from .round import Round


calss Game(object):

    def __init__(self, id):
        self.id = id
        self.players = players
        self.words_used = []
        self.round = None
        self.board = None
        self.player_draw_ind = 0
        slef.start_new_round()

    def start_new_round(self):
        self.round = Round(self.get_word(), self.players[self.player_draw_ind])
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.end_round()
            self.end_game()

    def player_guess(self, player, guess):
        pass

    def player_disconnect(self, player):
        pass
    
    def skip(self):
        pass

    def round_end(self):
        pass

    def update_board(self):
        pass

    def get_word(self):
        pass

    def end_game(self):
        pass