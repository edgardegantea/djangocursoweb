from django.contrib import admin
from django.urls import path
from gestion.views import IndexView, AcercaDe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('acercade', AcercaDe.as_view(), name='acercade')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
