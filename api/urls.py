from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from api.views.api import (
    Board,
    EmailAPI,
    get_status,
)
from api.views.user import (
    RegisterAPI,
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
