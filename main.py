import random
import math
import pygame
from pygame.locals import *
from classes import *
from functions import *

if __name__ == "__main__":
    pygame.init()

    # COLORS
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Window
    background_image_path = "images/background.jpg"
    window = Window(800, 600, "Save Earth", background_image_path)

    # Earth
    earth_image_path = "images/earth.png"
    earth_image_path2 = "images/earth2.png"
    earth_image_path3 = "images/earth3.png"
    earth_image_path4 = "images/earth4.png"

    # Load Earth images
    earth_images = [
        pygame.image.load(earth_image_path).convert_alpha(),
        pygame.image.load(earth_image_path2).convert_alpha(),
        pygame.image.load(earth_image_path3).convert_alpha(),
        pygame.image.load(earth_image_path4).convert_alpha()
    ]
    earth_images = [pygame.transform.scale(image, (100, 100)) for image in earth_images]


    # asteroid
    asteroid_image_path = "images/asteroid.png"

    defensor_image_path = "images/shield.png"

    while True:
        earth = Earth(earth_images[0], window.width, window.height)

        image = pygame.image.load(defensor_image_path)
        image = pygame.transform.scale(image, (50, 50))
        image_rect = image.get_rect()

        asteroids = []
        asteroids_number = 15
        for i in range(asteroids_number):
            asteroid = generate_asteroid(window)
            asteroids.append(asteroid)
            
        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()

            # window.fill()
            window.blit()

            # draw earth
            if earth.health <= 0:
                earth.image = earth_images[4]
            elif earth.health <= 25:
                earth.image = earth_images[3]
            elif earth.health <= 55:
                earth.image = earth_images[2]
            elif earth.health <= 75:
                earth.image = earth_images[1]
            elif earth.health == 100:
                earth.image = earth_images[0]

            earth.draw(window)
            earth.draw_health_bar(window.get_surface())

            for asteroid in asteroids:
                asteroid.update()
                asteroid.draw(window.get_surface())
            
            for asteroid in asteroids[::]:
                if earth.collide_circle(asteroid):
                    earth.health -= 15
                    asteroids.remove(asteroid)
                if image_rect.colliderect(asteroid.rect):
                    if asteroid in asteroids:
                        asteroids.remove(asteroid)

            if len(asteroids) < asteroids_number :
        
                asteroid = generate_asteroid(window)
                asteroids.append(asteroid)

            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Actualización de la posición de la imagen
            image_rect.center = (mouse_x, mouse_y)
            window.draw(image, image_rect)

            if earth.health < 0:
                break

            pygame.display.update()
            pygame.time.Clock().tick(60)

        draw_text("Game Over", window.font, window.get_surface(), window.width, window.height, RED)
        draw_text("Press a key to play again", window.font, window.get_surface(), window.width, window.height + 50, RED)
        pygame.display.update()
        wait()