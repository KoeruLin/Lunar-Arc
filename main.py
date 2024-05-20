import pygame
import random
from defender import Defender

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

# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
rng = 0
pull = []
pull_amount = 10
inventory = []
summon_banner_check = False

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------

while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something

        x, y = pygame.mouse.get_pos()
        #print(x, y)

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
                    defender_common = Defender(random.randint(200, 300), random.randint(300, 400), random.randint(2000, 3000))
                    inventory.append(defender_common)

                elif 41 <= pull[i] <= 90:
                    defender_rare = Defender(random.randint(300, 400), random.randint(400, 500), random.randint(2500, 3500))
                    inventory.append(defender_rare)

                elif 91 <= pull[i] <= 98:
                    defender_epic = Defender(random.randint(400, 500), random.randint(500, 600), random.randint(3000, 4000))
                    inventory.append(defender_epic)

                elif pull[i] == 99 or pull[i] == 100:
                    defender_legendary = Defender(random.randint(500, 600), random.randint(600, 700), random.randint(3500, 4500))
                    inventory.append(defender_legendary)

            print(inventory)

            list.clear(pull)

        if event.type == pygame.QUIT:  # If user clicked close

            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not summon_banner_check and (530 <= x <= 800) and (400 <= y <= 500):
            summon_banner_check = True
            screen.blit(gacha_background, (0, 0))
            screen.blit(gacha_banner, (0, 0))
            screen.blit(exit_button, (0, 0))

        if summon_banner_check and event.type == pygame.MOUSEBUTTONDOWN and (30 <= x <= 130) and (30 <= y <= 60):
            summon_banner_check = False

    if not summon_banner_check:
        screen.blit(lobby_background, (0, 0))
        screen.blit(summon_ui, (315, 200))

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
