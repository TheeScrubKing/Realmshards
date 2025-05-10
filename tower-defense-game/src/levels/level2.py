# filepath: /tower-defense-game/tower-defense-game/src/levels/level2.py

class Level2:
    def __init__(self):
        self.enemy_waves = [
            {"type": "BasicEnemy", "count": 10, "spawn_time": 1},
            {"type": "FastEnemy", "count": 5, "spawn_time": 3},
            {"type": "BossEnemy", "count": 1, "spawn_time": 10}
        ]
        self.tower_positions = [(2, 3), (4, 5), (6, 1)]
        self.victory_condition = "Defeat all enemies"
        self.defeat_condition = "Enemies reach the base"

    def start_level(self):
        print("Starting Level 2")
        self.spawn_enemies()

    def spawn_enemies(self):
        for wave in self.enemy_waves:
            for _ in range(wave["count"]):
                print(f"Spawning {wave['type']}")

    def check_victory(self):
        # Logic to check if the player has won
        pass

    def check_defeat(self):
        # Logic to check if the player has lost
        pass

# Example usage
if __name__ == "__main__":
    level2 = Level2()
    level2.start_level()