from typing import List

from mastermind.domain import Game, Guess

"""
Your tests here
"""


class TestFeedback:

    def test_feedback1(self):
        new_game = Game(1, None, 4, 4, ["orange", "orange", "orange", "white"], 4, "running",
                        ([], 0, 0))
        black_pegs, white_pegs = new_game._feedback(["orange", "white", "white", "white"])
        assert black_pegs == 2
        assert white_pegs == 0

    def test_feedback2(self):
        new_game = Game(1, None, 4, 4, ["white", "blue", "white", "blue"], 4, "running",
                        ([], 0, 0))
        black_pegs, white_pegs = new_game._feedback(["blue", "white", "blue", "white"])
        assert black_pegs == 0
        assert white_pegs == 4

    def test_feedback3(self):
        new_game = Game(1, None, 4, 4, ["blue", "blue", "blue", "red"], 4, "running",
                        ([], 0, 0))
        black_pegs, white_pegs = new_game._feedback(["blue", "blue", "red", "blue"])
        assert black_pegs == 2
        assert white_pegs == 2

    def test_feedback4(self):
        new_game = Game(1, None, 4, 4, ["red", "blue", "green", "green"], 4, "running",
                        ([], 0, 0))
        black_pegs, white_pegs = new_game._feedback(["blue", "blue", "blue", "red"])
        assert black_pegs == 1
        assert white_pegs == 1

    def test_feedback5(self):
        new_game = Game(1, None, 4, 4, ["blue", "blue", "blue", "red"], 4, "running",
                        ([], 0, 0))
        black_pegs, white_pegs = new_game._feedback(["red", "blue", "green", "green"])
        assert black_pegs == 1
        assert white_pegs == 1

    def test_feedback6(self):
        new_game = Game(1, None, 4, 4, ["green", "blue", "blue", "red"], 4, "running",
                        ([], 0, 0))
        black_pegs, white_pegs = new_game._feedback(["green", "blue", "red", "blue"])
        assert black_pegs == 2
        assert white_pegs == 2

    def test_feedback7(self):
        new_game = Game(1, None, 4, 4, ["red", "red", "red", "red"], 4, "running",
                        ([], 0, 0))
        black_pegs, white_pegs = new_game._feedback(["blue", "yellow", "orange", "blue"])
        assert black_pegs == 0
        assert white_pegs == 0

    def test_feedback8(self):
        new_game = Game(1, None, 4, 4, ["red", "green", "green", "blue"], 4, "running",
                        ([], 0, 0))
        black_pegs, white_pegs = new_game._feedback(["red", "green", "green", "blue"])
        assert black_pegs == 4
        assert white_pegs == 0
