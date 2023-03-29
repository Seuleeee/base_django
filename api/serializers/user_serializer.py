from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwagrs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data
        )
        return user
