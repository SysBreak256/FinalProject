class Scoreboard():

    def __init__(self):
        self.player1scorefull = 0
        self.player2scorefull = 0
        self.player3scorefull = 0
        self.player4scorefull = 0


    def score(self, player1pos, player2pos, player3pos, player4pos):
        player1score = 960 - player1pos
        player2score = 960 - player2pos
        player3score = 960 - player3pos
        player4score = 960 - player4pos

        self.player1scorefull += player1score
        self.player2scorefull += player2score
        self.player3scorefull += player3score
        self.player4scorefull += player4score


    def updateScores(self, player1pos, player2pos, player3poos, player4pos):
        print(player1pos, player2pos, player3poos, player4pos)
        print(player1scorefull, player2scorefull, player3scorefull, player4scorefull)
        score()

    def drawscoreboard(self):





