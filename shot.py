import pygame
import random


class Shot:
    def __init__(self, main, t0):
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = self.screen.get_rect()

        self.y = self.screen_rect.bottom
        self.x = random.randint(0, self.settings.WIDTH)

        # initialize:
        self.center = (self.x, self.y)
        self.radius = self.settings.s_radius
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = (r, g, b)
        # get initial time in seconds
        self.initial_time = t0
        self.y_speed = -10
        self.v0 = random.randint(5, 10)

    def draw_shot(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

    def move_shot(self, tf):
        # if self.y_speed < 0:
        interval = (tf - self.initial_time)
        self.y_speed = -self.v0 + self.settings.gravity * interval
        self.y += self.y_speed
        self._update_center()

    def _update_center(self):
        self.center = (self.x, self.y)
