from typing import List

from mastermind.domain import Game

from mastermind.models import GameModel


class Games:

    @staticmethod
    def all() -> List[Game]:
        game_model_list = GameModel.objects.all()
        game_list = list()
        for game_model in game_model_list:
            game = game_model.to_domain()
            game_list.append(game)
        return game_list

    @staticmethod
    def save(game: Game) -> None:
        game_model = GameModel.from_domain(game)
        game_model.save()

    @staticmethod
    def get(id: int) -> Game:
        game_model = GameModel.objects.get(pk=id)
        game = game_model.to_domain()
        return game
