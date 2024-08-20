import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from status_display import display_menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return 
            
        for item in updatable:
            item.update(dt)
            pygame.display.update()
          
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                if player.player_lives == 0:
                    print("Game over!")
                    sys.exit()
                else: 
                    player.player_lives -= 1
                    player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    asteroid_field.reset(asteroid, asteroids)
                    
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()

        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip() 

        # limit the framerate to 60 FPS       
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()