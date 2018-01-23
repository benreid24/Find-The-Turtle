import pygame
from . import main_game


class StartMenu:
    def __init__(self):
        print('StartMenu created')

    def run(self, game):
        print('StartMenu running. Press SPACE to continue')
        while not pygame.key.get_pressed()[pygame.K_SPACE]:
            if game.process_events() != game.STATUS_OK:
                return
            pygame.time.wait(100)

        pygame.time.wait(500)
        game.next_state = main_game.create()


def create():
    return StartMenu()
