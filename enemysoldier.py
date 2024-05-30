import pygame

class EnemySoldier:
    def __init__(self, health, defense, x, y):
        self.health = health
        self.atk_spd = 1
        self.defense = defense
        self.speed = 10
        self.block_count = 1
        self.x = x
        self.y = y
        self.enemy_sprite = pygame.image.load("enemy_1.png")
        self.enemy_sprite = pygame.transform.scale(self.enemy_sprite, (100, 75))
        enemy_sprite_get = self.enemy_sprite.get_size()
        self.hitbox = pygame.Rect(self.x, self.y, enemy_sprite_get[0], enemy_sprite_get[1])
