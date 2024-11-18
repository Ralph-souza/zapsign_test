from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DocumentViewSet


router = DefaultRouter()
router.register(r'documents/', DocumentViewSet, basename='document'),
router.register(r'documents/create/', DocumentViewSet, basename='create_document')
router.register(r'documents/<int:document_id>/update/', DocumentViewSet, basename="document_update_by_id")
router.register(r'documents/<int:document_id>/delete/', DocumentViewSet, basename='document_delete')

urlpatterns = [
    path('', include(router.urls)),
]
