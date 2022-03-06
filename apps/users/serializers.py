from rest_framework import serializers
from django.contrib.auth import get_user_model


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
