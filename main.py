import pygame
import random

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Helvetica', 40)

# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
rng = 0
pull = []
pull_amount = 10

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------

while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something

        if event.type == pygame.MOUSEBUTTONDOWN:

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

    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
