from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
