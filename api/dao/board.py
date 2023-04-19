from api.models.board import SampleBoard


class BoardDao:
    def create(self, params):
        return SampleBoard.objects.create(**params)
