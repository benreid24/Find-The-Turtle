import pygame


class Game:
    """Main game class. Stores all Game data statically and provides some base functionality
       Keeps a next_state variable that gets updated by game states. Once it is no longer a state
       the game exits
    """

    STATUS_OK = 0
    STATUS_ERROR = 1
    STATUS_CLOSE = 2

    def process_events(self):
        """Process PyGame Window events and return a State"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Game.STATUS_CLOSE
            # TODO Handle more stuff

        return Game.STATUS_OK

    def __init__(self, resolution):
        # Set this from child states before exiting to run as the next state.
        # This design allows a clean stack trace
        self.next_state = None

        self.status = Game.STATUS_OK
        self.window = pygame.display.set_mode(resolution)

    def run(self, begin_state):
        begin_state.run(self)
        while self.next_state is not None:
            tmp = self.next_state
            self.next_state = None
            tmp.run(self)
            if self.status != Game.STATUS_OK or self.process_events() != Game.STATUS_OK:
                break
