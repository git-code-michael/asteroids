import pygame
import circleshape
import constants
from shot import Shot

class Player(circleshape.CircleShape):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta_time):
        self.rotation += constants.PLAYER_TURN_SPEED * delta_time

    def update(self, delta_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(delta_time * -1)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED