from api.dao.board import BoardDao


class BoardService:
    def create(self, params):
        obj = BoardDao().create(params)
        return {'id': obj.pk}