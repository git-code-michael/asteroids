from circleshape import CircleShape
import pygame
import constants
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, 2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        split_asteroid_1_angle = self.velocity.rotate(random_angle)
        split_asteroid_2_angle = self.velocity.rotate(-random_angle)
        split_asteroid_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        split_asteroid_1 = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
        
        split_asteroid_1.velocity = split_asteroid_1_angle * 1.2
        split_asteroid_2.velocity = split_asteroid_2_angle * 1.2


