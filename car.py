"""
Author: Mubarak Idoko
Date: 2024-06-08

Car Class
"""

# import libraries
import math
from typing import Tuple
import pygame

# import from project
from constants import WIDTH, HEIGHT, RADIUS

# Car class
class Car:
    """Car class
    """
    def __init__(self, angle, speed, image):
        self.angle = angle
        self.speed = speed
        self.image = image

    def update(self):
        """Update the car's angle
        """
        self.angle += self.speed
        if self.angle >= 360:
            self.angle -= 360

    def draw(self, screen: pygame.Surface):
        """Draw car on screen

        Args:
            screen (pygame.Surface): The pygame screen to draw on
        """
        x, y = self.position()
        rotated_image = pygame.transform.rotate(self.image, -self.angle)
        screen.blit(rotated_image, rotated_image.get_rect(center=(int(x), int(y))))

    def position(self) -> Tuple[float, float]:
        """Get the car's position

        Returns:
            Tuple(float, float): The car's x and y coordinates
        """
        x = WIDTH // 2 + RADIUS * math.cos(math.radians(self.angle))
        y = HEIGHT // 2 + RADIUS * math.sin(math.radians(self.angle))
        return x, y
