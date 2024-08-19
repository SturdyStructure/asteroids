# This allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Starting asteroids!")
                print(f"Screen width: {SCREEN_WIDTH}")
                print(f"Screen height: {SCREEN_HEIGHT}")
                return



if __name__ == "__main__":
    main()