from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from .models import Sections
from .serializers import SectionSerializer
from .permissions import IsOwner


# Create your views here.
# class SectionAPIView(ListCreateAPIView):
#     queryset = Sections.objects.filter(parent__isnull=True)
#     serializer_class = SectionSerializer

class SectionAPIView(ListCreateAPIView):
    serializer_class = SectionSerializer
    queryset = Sections.objects.filter(parent__isnull=True)
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class SectionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Sections.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, )
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
