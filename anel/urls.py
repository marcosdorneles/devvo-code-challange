from django.urls import path
from .views import anel_detail, criar_anel, listar_aneis
from anel import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:pk>/', views.detail, name='detail'),
    path('aneis/', listar_aneis, name='listar_aneis'),
    path('aneis/create/', criar_anel, name='criar_anel'),
    path('aneis/<int:pk>/', anel_detail, name='anel_detail'),
]
