import time

time = time.time()


class Defender:
    def __init__(self, attack, defense, health, x, y):
        self.block = 3
        self.attack = attack
        self.defense = defense
        self.atk_spd = 1
        self.health = health
        self.x = x
        self.y = y

    def blocked_enemy(self, block_count, enemy_hp):
        time_2 = time.time()
        time_delay = time - time_2

        self.block -= block_count

        while enemy_hp > 0:
            if time_delay < self.atk_spd:
                enemy_hp -= self.attack
                self.atk_spd += self.atk_spd

    def defense_reduction(self, enemy_attack, enemy_atk_spd):
        time_3 = time.time()
        time_delay_2 = time - time_3

        if time_delay_2 < enemy_atk_spd:
            damage_reduction = abs(self.defense - enemy_attack)
            self.health -= damage_reduction

    def move(self, x_coordinate, y_coordinate):
        while self.x != x_coordinate:
            self.x += 2

            while self.y != y_coordinate:
                self.y += 2
