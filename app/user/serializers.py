from rest_framework import serializers
from core import models
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _


class UserSerializer(serializers.ModelSerializer):
    """Serializer class for user"""
    class Meta:
        model = models.User
        fields = ['email', 'password']
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


class AuthTokenSerializer(serializers.ModelSerializer):
    """Serializer for AuthToken."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={
            'input_type': 'password'
        },
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate users."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            user=self.context.get('request'),
            username=email,
            password=password,
        )
        print(attrs)
        if not user:
            msg = _(
                'Sorry..We are unable to authenticate \n'
                'your with your credential'
            )
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
