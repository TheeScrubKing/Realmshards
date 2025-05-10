class BasicEnemy:
    def __init__(self):
        self.health = 100
        self.speed = 1
        self.damage = 10

    def move(self):
        # Logic for moving the enemy along the path
        pass

class FastEnemy(BasicEnemy):
    def __init__(self):
        super().__init__()
        self.health = 80
        self.speed = 2

class BossEnemy(BasicEnemy):
    def __init__(self):
        super().__init__()
        self.health = 300
        self.speed = 0.5
        self.damage = 20

    def special_ability(self):
        # Logic for boss special ability
        pass

class ArmoredEnemy(BasicEnemy):
    def __init__(self):
        super().__init__()
        self.health = 150
        self.speed = 0.8
        self.armor = 20

    def take_damage(self, amount):
        effective_damage = max(0, amount - self.armor)
        self.health -= effective_damage

class FlyingEnemy(BasicEnemy):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.speed = 1.5
        self.flying = True

    def move(self):
        # Logic for flying movement
        pass