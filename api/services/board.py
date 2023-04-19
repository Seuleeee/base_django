from api.repos.board import sample_board_repo


class BoardService:
    def get(self, pk: int):
        return sample_board_repo.get(pk)
    def get_multi(self):
        return sample_board_repo.get_multi(id__in=[2, 3])
