from api.models import Board


class BoardDao:
    def create(self, params):
        return Board.objects.create(**params)