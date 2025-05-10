class Level1:
    def __init__(self):
        self.enemy_waves = [
            {"type": "BasicEnemy", "count": 10, "spawn_time": 1},
            {"type": "FastEnemy", "count": 5, "spawn_time": 3},
            {"type": "BossEnemy", "count": 1, "spawn_time": 10},
        ]
        self.tower_positions = [
            (1, 2),
            (3, 4),
            (5, 6),
        ]
        self.victory_condition = "Defeat all enemies"
        self.defeat_condition = "Enemies reach the base"

    def start_level(self):
        print("Starting Level 1")
        self.spawn_enemies()
        self.place_towers()

    def spawn_enemies(self):
        for wave in self.enemy_waves:
            for _ in range(wave["count"]):
                print(f"Spawning {wave['type']}")

    def place_towers(self):
        for position in self.tower_positions:
            print(f"Placing tower at {position}")

    def check_victory(self):
        print(self.victory_condition)

    def check_defeat(self):
        print(self.defeat_condition)