import inspect
from collections import OrderedDict
from typing import (
    List,
    Dict,
    Any,
    Union,
)

from django.http import HttpRequest
from django.db.models.query import QuerySet
from rest_framework.pagination import PageNumberPagination
from rest_framework.serializers import Serializer


class PaginationUtil(PageNumberPagination):
    def __init__(
        self,
        *,
        queryset: QuerySet,
        request: HttpRequest,
        page_size: int=10
    ):
        """
        인스턴스를 초기화하는 메소드입니다.

        Args:
            queryset (QuerySet): 쿼리셋 객체.
            request (HttpRequest): HTTP 요청 객체.
            page_size (int, optional): 페이지 크기. 기본값은 10입니다.

        Returns:
            None

        Raises:
            None
        """
        self.page_size: int = page_size
        self._queryset: QuerySet = queryset
        self._request: HttpRequest = request

    def get_response(
        self,
        *,
        serializer: Union[Serializer, Any]=None
    ):
        """
        Pagination이 적용 된 응답을 반환하는 메소드입니다.
        페이지네이션된 쿼리셋을 가져오고, 직렬화된 데이터를 생성한 뒤, 해당 데이터로 구성된 페이지네이션된 응답 객체를 반환합니다.
        DjangoRestFramework의 BaseSerializer를 상속받은 Serializer를 인자로 받거나, 그렇지 않은 경우 모두 사용 가능합니다.

        Args:
            serializer (Union[Serializer, Any], optional): 사용할 직렬화 객체. 기본값은 None입니다.

        Returns:
            Response: pagination, 직렬화 된 data로 구성된 응답 객체.

        Raises:
            None
        """
        paginated_queryset = self.paginate_queryset(self._queryset, self._request)
        serialized_data = self._get_serialized_data(paginated_queryset=paginated_queryset, serializer=serializer)
        return self._build_response(serialized_data=serialized_data)

    def _get_serialized_data(
        self,
        *,
        paginated_queryset: QuerySet,
        serializer: Serializer = None,
    ) -> List[Dict[str, Any]]:
        """
        페이지네이션된 쿼리셋을 직렬화된 데이터로 변환하여 반환하는 내부 메소드입니다.

        인자로 받아온 serializer 객체가 Serializer 클래스의 서브클래스인지 확인하고,
        맞다면 쿼리셋을 해당 직렬화 객체를 사용하여 직렬화된 데이터로 변환하여 반환합니다.
        만약 받아온 serializer 객체가 None이거나 Serializer 클래스의 서브클래스가 아니라면,
        _get_serialized_data_from_queryset() 메소드를 사용하여 쿼리셋으로부터 직렬화된 데이터를 가져옵니다.

        Args:
            paginated_queryset (QuerySet): pagination 된 queryset 객체.
            serializer (Serializer, optional): 사용할 직렬화 객체. 기본값은 None입니다.

        Returns:
            List[Dict[str, Any]]: 직렬화 된 data로 구성된 dictionary list.

        Raises:
            None
        """
        if (inspect.isclass(serializer)) and issubclass(serializer, Serializer):
            return serializer(paginated_queryset, many=True).data
        else:
            return self._get_serialized_data_from_queryset(queryset=paginated_queryset)

    @staticmethod
    def _get_serialized_data_from_queryset(
        *,
        queryset: QuerySet,
    ) -> List[Dict[str, Any]]:
        """
        쿼리셋으로부터 직렬화된 데이터를 추출하여 반환하는 내부 메소드입니다.

        인자로 받아온 queryset 객체에서 field를 추출하여 각 객체의 field 값을 dictionary로 구성한 뒤,
        이러한 dictionary들로 이루어진 list를 반환합니다.

        Args:
            queryset (QuerySet): 직렬화 할 queryset 객체.

        Returns:
            List[Dict[str, Any]]: 직렬화 된 data로 구성된 dictionary list.

        Raises:
            None
        """
        return [{
                    field.name: getattr(obj, field.name)
                    for field in obj._meta.fields
                }
                for obj in queryset]

    def _build_response(self, *, serialized_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        pagination 된 응답 딕셔너리를 구성합니다.

        Args:
            serialized_data (List[Dict[str, Any]]): 응답에 포함할 직렬화된 데이터.

        Returns:
            Dict[str, Any]: 페이지네이션된 응답 딕셔너리로, count, 페이지 수, 페이지 크기, 다음 링크, 이전 링크, 그리고 직렬화된 결과를 포함합니다.
            - TODO: Dictionary에 사용한 Key 이름은 Client 측과 협의하여 변경해 사용하시면 됩니다.
        """
        return {
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'page_size': self.page_size,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': serialized_data
        }
