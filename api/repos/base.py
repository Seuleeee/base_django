from typing import TypeVar, Generic, Type, Optional, Any

from api.models.base import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepo(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD 모음 으로써 기본적인 get, get_multi, create, bulk_create, update, delete 를 담당
        """
        self.model = model

    def create(self, *, created_data: CreateSchemaType):
        """ Unpacking 가능한 Dictionary Type """
        instance = self.model.objects.create(**created_data)
        return instance

    def get(self, pk: Any) -> Optional[ModelType]:
        """ Model 을 직렬화 하지 않고 반환 """
        try:
            instance = self.model.objects.get(pk=pk)
            return instance
        except self.model.DoesNotExist:
            raise self.model.DoesNotExist

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

    def update(self, *, updated_data: CreateSchemaType, pk: int):
        """ Unpacking 가능한 Dictionary Type """
        instance = self.get(pk=pk)
        for field, value in updated_data.items():
            setattr(instance, field, value)

        instance.save()

        return instance

    def delete(self, *, pk: int):
        instance = self.get(pk=pk)
        instance.delete()
        return instance
