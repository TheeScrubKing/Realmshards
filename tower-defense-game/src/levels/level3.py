# filepath: /tower-defense-game/tower-defense-game/src/levels/level3.py

class Level3:
    def __init__(self):
        self.enemy_waves = [
            {"type": "BasicEnemy", "count": 10, "spawn_time": 1},
            {"type": "FastEnemy", "count": 5, "spawn_time": 2},
            {"type": "BossEnemy", "count": 1, "spawn_time": 5}
        ]
        self.tower_positions = [(2, 3), (4, 5), (6, 1)]
        self.victory_condition = "Defeat all enemies"
        self.defeat_condition = "Enemies reach the base"

    def setup_level(self):
        print("Setting up Level 3")
        print(f"Enemy Waves: {self.enemy_waves}")
        print(f"Tower Positions: {self.tower_positions}")
        print(f"Victory Condition: {self.victory_condition}")
        print(f"Defeat Condition: {self.defeat_condition}")

    def start_level(self):
        self.setup_level()
        # Logic to start the level would go here

# Example of how to use the Level3 class
if __name__ == "__main__":
    level3 = Level3()
    level3.start_level()