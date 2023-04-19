from api.models.board import SampleBoardModel
from api.repos.base import BaseRepo


class SampleBoardRepo(BaseRepo[SampleBoardModel]):
    def create(self, params):
        pass


sample_board_repo = SampleBoardRepo(SampleBoardModel)
