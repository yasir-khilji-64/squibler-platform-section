from django.contrib import auth
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8,
        max_length=30,
        write_only=True,
    )
    gravatar_url = serializers.URLField(
        read_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'email',
            'password',
            'gravatar_url',
            'created_at',
        ]

    def validate(self, attrs):
        '''
        Email field validation is already done
        using models, so there is no need to
        check for valid email here, and we
        can return attributes.
        '''
        return attrs

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(
        min_length=8,
        max_length=30,
        write_only=True
    )
    gravatar_url = serializers.URLField(
        max_length=128,
        read_only=True,
    )
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'password',
            'gravatar_url',
            'refresh',
            'access'
        ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials.')
        if not user.is_active:
            raise AuthenticationFailed(
                'Account disabled. Contact squibler admin'
            )

        refresh = user.token()
        return {
            "email": user.email,
            "gravatar_url": user.gravatar_url,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
