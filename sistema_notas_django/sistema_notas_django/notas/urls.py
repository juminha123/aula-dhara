from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),
    path('notas/nova/', views.criar_nota, name='criar_nota'),
    path('notas/<int:id>/editar/', views.editar_nota, name='editar_nota'),
    path('notas/<int:id>/excluir/', views.excluir_nota, name='excluir_nota'),
]
