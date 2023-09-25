class Round(object):
    def __init__(self, word, Player_drawing):
        self.word = word
        self.player_drawing = Player_drawing
        self.player_guessd = []
        self.skips = 0
        self.player_scores = {player = 0 for player in players}
        self.time = 0

    def guess(self, player,wrd):
        return wrd == self.word