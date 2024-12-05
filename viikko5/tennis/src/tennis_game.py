class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.prints = ["Love", "Fifteen", "Thirty", "Forty"]

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.deuce()
        
        if self.m_score1 > 3 or self.m_score2 > 3:
            return self.more_than_three_points()

        return f"{self.prints[self.m_score1]}-{self.prints[self.m_score2]}"
    
    def deuce(self):
        if self.m_score1<3:
            return f"{self.prints[self.m_score1]}-All"
        return "Deuce"
    
    def more_than_three_points(self):
        if abs(self.m_score1 - self.m_score2) == 1:
            if self.m_score1 > self.m_score2:
                return f"Advantage {self.player1_name}"
            return f"Advantage {self.player2_name}"
        
        if self.m_score1 > self.m_score2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"  

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1
