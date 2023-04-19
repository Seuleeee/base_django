from typing import TypeVar, Generic, Type, Optional, Any, List

from api.models.base import BaseModel


ModelType = TypeVar("ModelType", bound=BaseModel)


class BaseRepo(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD 모음 으로써 기본적인 get, get_multi, create, bulk_create, update, delete 를 담당
        """
        self.model = model

    def get(self, pk: Any) -> Optional[ModelType]:
        """ Model 을 직렬화 하지 않고 반환 """
        return self.model.objects.get(pk=pk)

    def get_multi(self, **kwargs) -> Optional[ModelType]:
        """
        Model 을 직렬화 하지 않고 반환
        호출 시, Filter로 적용하고자 하는 값들을 넣어서 사용
        * 사용 예시
            1. some_repo.get_multi(id=pk)
            2. some_repo.get_multi(id__in=[2, 3])
            3. some_repo.get_multi(id=pk, content="blahblah")
        """
        return self.model.objects.filter(**kwargs)

