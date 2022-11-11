from typing import List

from django.db import models

from mastermind.domain import Game, Guess


class GameModel(models.Model):

    id = models.AutoField(primary_key=True)
    reference = models.CharField(max_length=20)
    num_slots = models.PositiveIntegerField()
    num_colors = models.PositiveIntegerField()
    secret_code = models.ExpressionList(List[str])
    max_guesses = models.PositiveIntegerField()
    status = models.CharField(max_length=20)
    guesses = models.ExpressionList(List[str])

    def __init__(self, id: int, reference: str, num_slots: int, num_colors: int, secret_code: List[str],
                 max_guesses: int, status: str, guesses: List[Guess]):
        self.id = id
        self.reference = reference
        self.num_slots = num_slots
        self.num_colors = num_colors
        self.secret_code = secret_code
        self.max_guesses = max_guesses
        self.status = status
        self.guesses = guesses

    def to_domain(self) -> Game:
        return Game(self.id, self.reference, self.num_slots, self.num_colors, self.secret_code, self.max_guesses,
                    self.status, self.guesses)

    @staticmethod
    def from_domain(game: Game):
        return GameModel(game.id, game.reference, game.num_slots, game.num_colors, game.secret_code, game.max_guesses,
                         game.status, game.guesses)
