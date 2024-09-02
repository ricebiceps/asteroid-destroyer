import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shot, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for obj in updatable:
            obj.update(dt)

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroid:
            if(player.is_collided(obj)):
                print("GAME OVER")
                return
            for bullet in shot:
                if obj.is_collided(bullet):
                    obj.split()
                    bullet.kill()

        pygame.display.flip()
        
        #limit the fps to 60
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
