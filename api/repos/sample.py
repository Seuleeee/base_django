from api.models.sample import (
    SampleModel,
    SampleFileModel,
)
from api.repos.base import BaseRepo


class SampleRepo(BaseRepo[SampleModel]):
    def create(self, params):
        pass


class SampleFileRepo(BaseRepo[SampleFileModel]):
    def create(self, params):
        pass



sample_repo = SampleRepo(SampleModel)
sample_file_repo = SampleFileRepo(SampleFileModel)
