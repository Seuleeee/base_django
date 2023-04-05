import pytest
from unittest.mock import MagicMock

from django.contrib.auth.models import User


@pytest.fixture
def user_model():
    user_model_mock = MagicMock(spec=User)
    user_model_mock.name = "TestUser"
    user_model_mock.email = "test@gmail.com"

    return user_model_mock


def test_user_model(user_model):
    assert user_model.name == "TestUser"
    assert user_model.email == "test@gmail.com"

