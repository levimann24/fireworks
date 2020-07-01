import pygame
import random
import math


class Particle:
    def __init__(self, explosion):
        # initialize main settings
        self.settings = explosion.settings
        self.screen = explosion.screen
        self.screen_rect = self.screen.get_rect()

        # intialize particles
        self.center = explosion.center
        self.color = explosion.color
        self.radius = self.settings.p_radius
        self.x = self.center[0]
        self.y = self.center[1]

        self.direction = 2*math.pi*random.uniform(0, 1)
        self.speed = 4 * random.uniform(0.1, 1)
        self.t0 = explosion.t0

    def draw_particle(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

    def move_particle(self, tf):
        v0_x = self.speed * math.cos(self.direction)
        v0_y = self.speed * math.sin(self.direction)

        interval = tf - self.t0
        x_speed = v0_x
        y_speed = v0_y + self.settings.gravity * interval

        self.x += x_speed
        self.y += y_speed

        self.center = (self.x, self.y)
