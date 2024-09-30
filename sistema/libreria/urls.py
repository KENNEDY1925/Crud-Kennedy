from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name= 'nosotros'),
    path('Libros',views.Libros, name='libros')

]
