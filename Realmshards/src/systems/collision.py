class CollisionSystem:
    def __init__(self):
        self.collisions = []

    def check_collision(self, tower, enemy):
        # Simple bounding box collision detection
        if (tower.x < enemy.x + enemy.width and
            tower.x + tower.width > enemy.x and
            tower.y < enemy.y + enemy.height and
            tower.y + tower.height > enemy.y):
            return True
        return False

    def detect_collisions(self, towers, enemies):
        self.collisions.clear()
        for tower in towers:
            for enemy in enemies:
                if self.check_collision(tower, enemy):
                    self.collisions.append((tower, enemy))

    def resolve_collisions(self):
        for tower, enemy in self.collisions:
            enemy.take_damage(tower.damage)
            # Additional logic for what happens on collision can be added here
            if enemy.health <= 0:
                enemy.mark_for_removal()