class BasicTower:
    def __init__(self, damage, range):
        self.damage = damage
        self.range = range

    def attack(self, enemy):
        if self.is_in_range(enemy):
            enemy.take_damage(self.damage)

    def is_in_range(self, enemy):
        # Placeholder for range checking logic
        return True  # Assume always in range for simplicity

    def upgrade(self):
        self.damage += 5
        self.range += 1