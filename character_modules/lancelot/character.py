from random import randint

class Lancelot:
    def __init__(self):
        self.name = ""
        self.health = 1
        # Remove self.health_max if not necessary
        self.health_max = 1

    def do_damage(self, enemy):
        damage = min(
            max(randint(0, self.health) - randint(0, enemy.health), 0),
            enemy.health)
        enemy.health = enemy.health - damage
        if damage == 0:
            print("{} evades {}'s attack.".format(enemy.name, self.name))
        else:
            print("{} hurts {}!".format(self.name, enemy.name))
        return enemy.health <= 0

# Assuming there is a Character class that Enemy inherits from
class Enemy(Character):
    def __init__(self, player):
        super().__init__()
        self.name = 'a goblin'
        self.health = randint(1, player.health)
