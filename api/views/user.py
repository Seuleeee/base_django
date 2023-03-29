from rest_framework import (
    generics,
    permissions,
)
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from api.serializers.user_serializer import (
    UserSerializer,
    RegisterSerializer,
)


class RegisterAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(
        self,
        request,
        *args,
        **kwargs
    ):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        result = {
            "user": UserSerializer(
                user,
                context=self.get_serializer_context()
            ).data,
        }

        return Response(result)
