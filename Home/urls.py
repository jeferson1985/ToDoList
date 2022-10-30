from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('addTask/', views.addTask, name='addTask'),
    path('addItem/', views.addItem, name='addItem'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('finalizar/<int:id>/', views.finalizar, name='finalizar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('buscar/', views.buscar, name='buscar'),
]
