from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.Home_View, name='home'),
    path('about/', views.About_View, name='about'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)