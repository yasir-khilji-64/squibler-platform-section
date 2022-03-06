from django.urls import path

from .views import SectionAPIView, SectionDetailAPIView


urlpatterns = [
    path('sections/', SectionAPIView.as_view(), name='sections'),
    path('sections/<int:id>/', SectionDetailAPIView.as_view(), name='section')
]
