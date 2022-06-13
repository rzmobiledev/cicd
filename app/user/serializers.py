from rest_framework.serializers import ModelSerializer
from core import models


class UserSerializer(ModelSerializer):
    """Serializer class for user"""
    class Meta:
        model = models.User
        fields = ['email', 'password', 'username']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5
            }
        }

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return models.User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
