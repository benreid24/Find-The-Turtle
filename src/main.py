import config
import core.game
from core.states import start_menu


def main():
    game = core.game.Game(config.SCREEN_RESOLUTION)
    game.run(start_menu.create())


if __name__ == '__main__':
    main()
