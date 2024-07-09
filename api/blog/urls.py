from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),  # Ejemplo de URL para lista de usuarios
    path('photos/', views.PhotoListView.as_view(), name='photo-list'),  # Ejemplo de URL para lista de fotos
    # Añade más URLs para otras vistas de tu aplicación
]