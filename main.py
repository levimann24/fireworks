import pygame
import sys
import settings
import shot


class Fireworks:
    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()

        # initialize the screen
        self.screen = pygame.display.set_mode(
            (self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption("Fireworks for Our Freedom!")

        # initialize shot
        self.shot_group = []
        self._create_shots()

    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def on_loop(self):
        for shot in self.shot_group:
            tf = pygame.time.get_ticks()/1000
            shot.move_shot(tf)
        self._delete_shots()

    def on_render(self):
        self.screen.fill(self.settings.bg_color)
        for shot in self.shot_group:
            shot.draw_shot()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        while True:
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def _create_shots(self):
        while len(self.shot_group) < self.settings.n_shots:
            t0 = pygame.time.get_ticks()/1000
            n_shot = shot.Shot(self, t0)
            self.shot_group.append(n_shot)

    def _delete_shots(self):
        for shot in self.shot_group:
            if shot.y_speed >= 0:
                self.shot_group.remove(shot)
        self._create_shots()

    def _create_explosion(self):
        pass


if __name__ == "__main__":
    game = Fireworks()
    game.on_execute()
