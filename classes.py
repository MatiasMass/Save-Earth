import math
import pygame 
from pygame.locals import *

pygame.font.init()

class Window:
    
    font = pygame.font.SysFont("Arial", 30)

    def __init__(self, width, height, caption, image_path):
        self.width = width
        self.height = height
        self.caption = caption
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load(image_path).convert()
        self.background_image = pygame.transform.scale(self.background, (self.width, self.height))
        pygame.display.set_caption(self.caption)

    def fill(self):
        self.surface.fill((255, 255, 255))

    def blit(self):            
        self.surface.blit(self.background_image, (0, 0))

    def draw(self, image, rect):
        self.surface.blit(image, rect)

    def get_surface(self):
        return self.surface
    
class Earth:
    width = 100
    height = 100
    radius = 50
    color = (0, 0, 0)

    def __init__(self, image, windowWidth, windowHeight):
        self.image = image
        self.circle_rect = self.image.get_rect(center=(windowWidth // 2, windowHeight // 2))
        self.health = 100

    def draw(self, window):
        self.circle = pygame.draw.circle(window.get_surface(), self.color, self.circle_rect.center, self.radius)
        window.draw(self.image, self.circle)

    def collide_circle(self, asteroud):
        if math.sqrt((asteroud.rect.x - self.circle.x) ** 2 + (asteroud.rect.y - self.circle.y) ** 2) <= self.radius:
            return True
    
    def draw_health_bar(self, surface):
        bar_width = self.circle.width  # Anchura de la barra de vida igual al tamaño del asteroide
        bar_height = 5  # Altura de la barra de vida
        bar_x = self.circle.x  # Posición X de la barra de vida igual a la posición X del asteroide
        bar_y = self.circle.y + self.circle.width + 5  # Posición Y de la barra de vida debajo del asteroide

        # Calcula el porcentaje de vida actual del asteroide
        health_percentage = self.health / 100.0

        # Calcula la longitud del rectángulo de la barra de vida según el porcentaje de vida
        bar_length = int(bar_width * health_percentage)

        # Dibuja el fondo de la barra de vida (en rojo)
        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))

        # Dibuja la parte llena de la barra de vida (en verde)
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_length, bar_height))


# class Earth:
#     width = 100
#     height = 100
#     radius = 50
#     color = (0, 0, 0)

#     def __init__(self, image_path, windowWidth, windowHeight):
#         self.image = pygame.image.load(image_path).convert_alpha()
#         self.image = pygame.transform.scale(self.image, (self.width, self.height))
#         self.circle_rect = self.image.get_rect(center=(windowWidth // 2, windowHeight // 2))
#         self.health = 100

#     def draw(self, window):
#         window.draw(self.image, self.circle_rect)

#     def collide_circle(self, asteroid):
#         if math.sqrt((asteroid.rect.x - self.circle_rect.x) ** 2 + (asteroid.rect.y - self.circle_rect.y) ** 2) <= self.radius:
#             return True

#     def draw_health_bar(self, surface):
#         bar_width = self.circle_rect.width  # Anchura de la barra de vida igual al tamaño del asteroide
#         bar_height = 5  # Altura de la barra de vida
#         bar_x = self.circle_rect.x  # Posición X de la barra de vida igual a la posición X del asteroide
#         bar_y = self.circle_rect.y + self.circle_rect.width + 5  # Posición Y de la barra de vida debajo del asteroide

#         # Calcula el porcentaje de vida actual del asteroide
#         health_percentage = self.health / 100.0

#         # Calcula la longitud del rectángulo de la barra de vida según el porcentaje de vida
#         bar_length = int(bar_width * health_percentage)

#         # Dibuja el fondo de la barra de vida (en rojo)
#         pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, bar_width, bar_height))

#         # Dibuja la parte llena de la barra de vida (en verde)
#         pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, bar_length, bar_height))
                                                
class Asteroid:
    width = 30
    height = 80
    color = (255, 255, 255)

    def __init__(self, start_x, start_y, target_x, target_y, angle, speed, size):
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.surface.get_rect(topleft=(start_x, start_y))
        self.rect.x = start_x
        self.rect.y = start_y
        self.target_x = target_x
        self.target_y = target_y
        self.angle = angle
        self.speed = speed
        self.size = size
        self.dx = math.cos(math.radians(self.angle)) * self.speed
        self.dy = -math.sin(math.radians(self.angle)) * self.speed

    def draw(self, window):
    #     # angle_to_target = math.degrees(math.atan2(self.target_y - self.rect.centery, self.target_x - self.rect.centerx))
    #     # rotated_surface = pygame.transform.rotate(self.surface, -angle_to_target)
    #     # rotated_rect = rotated_surface.get_rect(center=self.rect.center)
    #     window.get_surface().blit(rotated_surface, rotated_rect)
        pygame.draw.circle(window, self.color, (self.rect.x, self.rect.y), self.size)  # Dibuja un rectángulo rojo en la superficie


    def update(self):
        self.rect.x += self.speed * math.cos(math.radians(self.angle))
        self.rect.y += self.speed * math.sin(math.radians(self.angle))
