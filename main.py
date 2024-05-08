import pygame
import random

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Helvetica', 40)

summon_ui = pygame.image.load("pixil-frame-0.png")
summon_ui = pygame.transform.scale(summon_ui, (500, 400))

exit_button = pygame.image.load("exit-button.png.png")
exit_button = pygame.transform.scale(exit_button, (150, 100))

# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
rng = 0
pull = []
pull_amount = 10
summon_banner_check = False

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------

while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something

        x, y = pygame.mouse.get_pos()
        print(x, y)

        if event.type == pygame.MOUSEBUTTONDOWN and summon_banner_check:

            for i in range(pull_amount):
                rng = random.randint(1, 100)
                pull.append(rng)

            for i in range(len(pull)):

                if pull[i] <= 40:
                    print("You got a common!")

                elif 41 <= pull[i] <= 90:
                    print("You got a rare!")

                elif 91 <= pull[i] <= 98:
                    print("You got a epic!")

                elif pull[i] == 99 or pull[i] == 100:
                    print("You got a legendary!")

            list.clear(pull)

        if event.type == pygame.QUIT:  # If user clicked close

            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not summon_banner_check and (530 <= x <= 800) and (400 <= y <= 500):
            summon_banner_check = True
            print("True")
            screen.fill((200, 100, 200))
            screen.blit(exit_button, (0, 0))

        if summon_banner_check and event.type == pygame.MOUSEBUTTONDOWN and (30 <= x <= 130) and (30 <= y <= 60):
            summon_banner_check = False

    if not summon_banner_check:
        screen.blit(summon_ui, (315, 200))

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
