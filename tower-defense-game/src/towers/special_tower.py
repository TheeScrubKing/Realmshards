class SpecialTower:
    def __init__(self, damage, range, special_effect):
        self.damage = damage
        self.range = range
        self.special_effect = special_effect

    def attack(self, enemy):
        # Implement attack logic with special effect
        enemy.take_damage(self.damage)
        self.apply_special_effect(enemy)

    def apply_special_effect(self, enemy):
        if self.special_effect == "slow":
            enemy.speed *= 0.5  # Slow down the enemy
        elif self.special_effect == "burn":
            enemy.take_damage(self.damage * 0.1)  # Burn effect over time
        elif self.special_effect == "freeze":
            enemy.is_frozen = True  # Freeze the enemy temporarily

    def __str__(self):
        return f"SpecialTower(damage={self.damage}, range={self.range}, special_effect={self.special_effect})"