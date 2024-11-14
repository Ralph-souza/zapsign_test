from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signature/', include('apps.signature.urls'), name='signature'),
]
