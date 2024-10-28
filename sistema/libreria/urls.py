from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('Libros', views.Libros, name='libros'),
    path('Libros/crear', views.crear, name='crear'),
    path('Libros/editar/<int:id>/', views.editar, name='editar'),  # <-- Cambiado
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('Libros/editar<int:id>/', views.editar, name='editar'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
