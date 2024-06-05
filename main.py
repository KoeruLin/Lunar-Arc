import pygame
import random
from defender import Defender
from enemysoldier import EnemySoldier

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Helvetica', 40)

summon_ui = pygame.image.load("pixil-frame-0.png")
summon_ui = pygame.transform.scale(summon_ui, (500, 400))

exit_button = pygame.image.load("exit-button.png.png")
exit_button = pygame.transform.scale(exit_button, (150, 100))

lobby_background = pygame.image.load("background_lobby.gif")
lobby_background = pygame.transform.scale(lobby_background, (800, 600))

gacha_banner = pygame.image.load("lunar-arc-gacha-banner(wip)-pixilart (2).png")
gacha_banner = pygame.transform.scale(gacha_banner, (850, 650))

gacha_background = pygame.image.load("pngtree-rectangle-grey-background-image_354811.jpg")
gacha_background = pygame.transform.scale(gacha_background, (800, 600))

tutorial_map = pygame.image.load("pixilart-drawing.png")
tutorial_map = pygame.transform.scale(tutorial_map, (700, 525))

play_button = pygame.image.load("play_button.png")
play_button = pygame.transform.scale(play_button, (600, 450))

# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
rng = 0
pull = []
pull_amount = 10
limit = 0
inventory = []
x_coordinate, y_coordinate = (712, 10)
rarity = (0, 0, 0)
surface = pygame.display.set_mode((800, 600))
summon_banner_check = False
play_game_check = False

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------

while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something

        x, y = pygame.mouse.get_pos()
        print(x, y)

        if event.type == pygame.MOUSEBUTTONDOWN and summon_banner_check and ((430 <= x <= 565 and 520 <= y <= 565) or (600 <= x <= 700 and 520 <= y <= 570)):
            if 430 <= x <= 565 and 520 <= y <= 565:
                pull_amount = 1

            if 600 <= x <= 700 and 520 <= y <= 570:
                pull_amount = 10

            for i in range(pull_amount):
                rng = random.randint(1, 100)
                pull.append(rng)

            for i in range(len(pull)):

                if pull[i] <= 40:
                    defender_common = Defender(random.randint(200, 300), random.randint(300, 400), random.randint(2000, 3000), 0, 0, 1)
                    inventory.append(defender_common)
                    print("Common")

                elif 41 <= pull[i] <= 90:
                    defender_rare = Defender(random.randint(300, 400), random.randint(400, 500), random.randint(2500, 3500), 0, 0, 2)
                    inventory.append(defender_rare)
                    print("Rare")

                elif 91 <= pull[i] <= 98:
                    defender_epic = Defender(random.randint(400, 500), random.randint(500, 600), random.randint(3000, 4000), 0, 0, 3)
                    inventory.append(defender_epic)
                    print("Epic")

                elif pull[i] == 99 or pull[i] == 100:
                    defender_legendary = Defender(random.randint(500, 600), random.randint(600, 700), random.randint(3500, 4500), 0, 0, 4)
                    inventory.append(defender_legendary)
                    print("Legendary")

            list.clear(pull)
            print(inventory)

        if event.type == pygame.QUIT:  # If user clicked close

            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not summon_banner_check and not play_game_check and (530 <= x <= 800) and (400 <= y <= 500):
            summon_banner_check = True
            screen.blit(gacha_background, (0, 0))
            screen.blit(gacha_banner, (0, 0))
            screen.blit(exit_button, (0, 0))

        if event.type == pygame.MOUSEBUTTONDOWN and not play_game_check and not summon_banner_check and (510 <= x <= 800) and (190 <= y <= 290) and len(inventory) >= 1:
            play_game_check = True
            screen.fill((0, 0, 0))
            screen.blit(tutorial_map, (0, 0))
            screen.blit(exit_button, (0, 0))
            for i in range(1):
                enemies = EnemySoldier(6000, 300, 0, 80)
                screen.blit(enemies.enemy_sprite, (enemies.x, enemies.y))

            for i in range(len(inventory)):
                blit_defender = inventory[i]

                if blit_defender.rarity == 1:
                    rarity = (128, 128, 128)
                elif blit_defender.rarity == 2:
                    rarity = (0, 150, 255)
                elif blit_defender.rarity == 3:
                    rarity = (160, 32, 240)
                else:
                    rarity = (255, 215, 0)

                while limit < 3:
                    pygame.draw.rect(surface, rarity, pygame.Rect(x_coordinate, y_coordinate, 75, 70), 3)
                    screen.blit(blit_defender.defender_sprite, (x_coordinate, y_coordinate))
                    y_coordinate += 80
                    limit += 1


        if play_game_check and event.type == pygame.MOUSEBUTTONDOWN and (30 <= x <= 130) and (30 <= y <= 60):
            play_game_check = False

        if summon_banner_check and event.type == pygame.MOUSEBUTTONDOWN and (30 <= x <= 130) and (30 <= y <= 60):
            summon_banner_check = False

    if not summon_banner_check and not play_game_check:
        screen.blit(lobby_background, (0, 0))
        screen.blit(summon_ui, (315, 200))
        screen.blit(play_button, (345, 0))

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
