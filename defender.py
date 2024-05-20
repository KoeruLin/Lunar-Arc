import pygame

class Defender:
    def __init__(self, atk, defense, health):
        self.block = 3
        self.atk = atk
        self.defense = defense
        self.atk_spd = 1
        self.health = health