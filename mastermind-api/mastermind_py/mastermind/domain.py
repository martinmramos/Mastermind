import random
import uuid
from typing import List, Tuple, Optional


# from pydash import py_


class Colors:
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    ORANGE = "orange"
    BLACK = "black"
    WHITE = "white"
    PURPLE = "purple"
    TURQUOISE = "turquoise"


colors = [
    Colors.RED,
    Colors.BLUE,
    Colors.GREEN,
    Colors.YELLOW,
    Colors.ORANGE,
    Colors.WHITE,
    Colors.PURPLE,
    Colors.TURQUOISE,
]


class GameStatus:
    RUNNING = "running"
    WON = "won"
    LOST = "lost"


def create_reference() -> str:
    """Generate a default stream name.

    The stream name will be completely random, based on the UUID generator
    passed onto hex format and cutr down to 8 characters. Remeber, UUID4's
    are 32 characters in length, so we cut it
    """
    divider = 3  # Divided by 3 generates 8 characters, by 2, 16 characters
    random_uuid = uuid.uuid4()
    stream_name = random_uuid.hex[: int(len(random_uuid.hex) / divider)]
    return stream_name


class Guess:
    def __init__(self, code: List[str], black_pegs: int, white_pegs: int) -> None:
        self.code = code
        self.black_pegs = black_pegs
        self.white_pegs = white_pegs


class Game:
    def __init__(
        self,
        id: Optional[int],
        reference: str,
        num_slots: int,
        num_colors: int,
        secret_code: List[str],
        max_guesses: int,
        status: str,
        guesses: List[Guess],
    ):
        self.id = id
        self.reference = reference
        self.num_slots = num_slots
        self.num_colors = num_colors
        self.secret_code = secret_code
        self.max_guesses = max_guesses
        self.status = status
        self.colors = (
            [
                Colors.RED,
                Colors.BLUE,
                Colors.GREEN,
                Colors.YELLOW,
                Colors.ORANGE,
                Colors.WHITE,
                Colors.PURPLE,
                Colors.TURQUOISE
            ], num_colors)
        # py_.take(colors, num_colors)
        self.guesses = guesses

    def add_guess(self, code: List[str]) -> None:
        if self.status != GameStatus.RUNNING:
            raise Exception("Cannot add a new guess, the game is already finished")

        # TODO: Implement this. Call the _feedback function, and update the status of the game
        # depending on the result
        length = len(self.secret_code)
        if self._feedback(code) == [length, 0]:
            self.status = GameStatus.WON
        if len(self.guesses) == self.max_guesses:
            self.status = GameStatus.LOST
        else:
            self.status = GameStatus.RUNNING

    def _feedback(self, code: List[str]) -> Tuple[int, int]:
        """
        Compares the given code with the secret code of the game, and returns a tuple
        of the number of (black_pegs, white_pegs)
        """
        # TODO: Implement this
        black_pegs = 0
        white_pegs = 0
        new_secret_code = self.secret_code.copy()
        new_code = code.copy()
        for color, secret_color in zip(code, self.secret_code):
            if color.__eq__(secret_color):
                new_secret_code.remove(color)
                new_code.remove(color)
                black_pegs += 1
        for color1 in new_code:
            try:
                new_secret_code.index(color1)
            except ValueError:
                continue
            else:
                if color1.__eq__(new_secret_code.index(color1)):
                    white_pegs += 1
        return black_pegs, white_pegs

    @staticmethod
    def new(num_slots: int, num_colors: int, max_guesses: int) -> "Game":
        reference = create_reference().upper()
        chosen_colors = py_.take(colors, num_colors)
        secret_code = random.choices(chosen_colors, k=num_slots)
        return Game(
            None,
            reference,
            num_slots,
            num_colors,
            secret_code,
            max_guesses,
            GameStatus.RUNNING,
            [],
        )
