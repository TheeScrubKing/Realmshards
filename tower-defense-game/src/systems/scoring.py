class ScoringSystem:
    def __init__(self):
        self.score = 0

    def add_score(self, points):
        self.score += points
        print(f"Score updated: {self.score}")

    def get_score(self):
        return self.score

    def reset_score(self):
        self.score = 0
        print("Score reset to 0")