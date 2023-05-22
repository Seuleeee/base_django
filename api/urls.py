from django.urls import (
    path,
    include,
)
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from api.views.api import (
    Board,
    EmailAPI,
    get_status,
)
from api.views.user import (
    RegisterAPI,
)
from api.views.sample import (
    SampleFileView,
    SampleModelViewSet,
)

urlpatterns = [
    path('v1/boards/<int:pk>', Board.as_view()),
    path('v1/emails', EmailAPI.as_view()),
    path('v1/celery/tasks/<task_id>', get_status, name='get_status'),
]

urlpatterns += [
    path('v1/register', RegisterAPI.as_view(), name='Auth'),
    path('v1/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()
router.register(r'samples', SampleModelViewSet)

urlpatterns += [
    path('', include(router.urls)),
    path('samples/file', SampleFileView.as_view(), name='SampleFile'),
]
