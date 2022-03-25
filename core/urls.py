from django.urls import path
from . import views

urlpatterns = [
    path('', views.moradores),
    path('moradores', views.moradores),
    path('inquilino/<int:id>', views.inquilinoView, name="inquilino-view"),
    path('inserir/', views.inserir, name='inserir'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('deletar/<int:id>', views.deletar, name='delete'),

]
