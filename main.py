import pygame
import constants
from player import Player


def main():
    pygame.init()

    clock = pygame.time.Clock()
    delta_time = 0

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    
    player = Player(x = constants.SCREEN_WIDTH / 2, y = constants.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for object in updateable:
            object.update(delta_time)

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        delta_time = clock.tick(60) / 1000

if __name__ == "__main__":
    main()