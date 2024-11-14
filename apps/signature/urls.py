from django.urls import path

from .views import signature_view


urlpatterns = [
    path('signature/', signature_view, names='signature'),
]
