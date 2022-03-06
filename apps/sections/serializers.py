from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Sections


class SectionSerializer(serializers.ModelSerializer):
    subsections = RecursiveField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Sections
        fields = [
            'id',
            'title',
            'parent',
            'subsections'
        ]
