import sys
import pprint

BOARD_WIDTH = 10
BOARD_HEIGHT = 10
DEAD="*"
ALIVE="O"


class Board:
    def __init__(self):
        self.board: list[list[int]] = [
            [DEAD for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

    def update(self):
        pass

    def render(self):
        for row in self.board:
            for col in row:
                print(col, end=" ")

    def clear(self):
        pass


class Game:
    def __init__(self):
        self.running = False
        self.board = Board()

    def update(self, dt: float = 0.0):
        pass

    def render(self) -> None:
        self.clear()
        self.board.render()

    def clear(self) -> None:
        print("\033c", end="")


def main() -> int:
    game = Game()
    pprint(game.board.board)

    dt = 1.0 / 60.0
    frame_counter = 0

    while game.running:
        frame_counter += dt

        if frame_counter >= 1000.0:
            game.update(dt)
            game.render()
            frame_counter = 0.0


if __name__ == "__main__":
    sys.exit(main())
