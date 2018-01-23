import pygame


class MainGame:
    def __init__(self):
        print('MainGame created')

    def run(self, game):
        print('MainGame running. Press SPACE to continue')
        while not pygame.key.get_pressed()[pygame.K_SPACE]:
            if game.process_events() != game.STATUS_OK:
                return
            game.process_events()
            pygame.time.wait(100)


def create():
    return MainGame()
