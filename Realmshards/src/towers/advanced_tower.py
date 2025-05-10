class AdvancedTower(BasicTower):
    def __init__(self, damage, range, splash_damage, attack_speed):
        super().__init__(damage, range)
        self.splash_damage = splash_damage
        self.attack_speed = attack_speed

    def attack(self, enemies):
        for enemy in enemies:
            if self.is_in_range(enemy):
                enemy.take_damage(self.damage)
                self.deal_splash_damage(enemy)

    def deal_splash_damage(self, enemy):
        for nearby_enemy in self.get_nearby_enemies(enemy):
            nearby_enemy.take_damage(self.splash_damage)

    def get_nearby_enemies(self, enemy):
        # Logic to find nearby enemies within splash range
        pass

    def is_in_range(self, enemy):
        # Logic to check if the enemy is within the tower's range
        pass