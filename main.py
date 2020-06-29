import pygame
import sys
import settings


class Fireworks:
    def __init__(self):
        self.settings = settings.Settings()

        # initialize the screen
        self.screen = pygame.display.set_mode(
            (self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption("Fireworks for Our Freedom!")

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.kq:
                    sys.exit()

    def on_loop(self):
        pass

    def on_render(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        while True:
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    game = Fireworks()
    game.on_execute()
