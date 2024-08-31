import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        #override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_collided(self, other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position)

        if(distance >= self.radius + other.radius):
            return False
        
        return True
