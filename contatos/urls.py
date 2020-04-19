from django.urls import path
from . import views

app_name = 'contatos' 

urlpatterns = [
    path('', views.contatos_list, name='list'),
    path('redirect/<int:contato_id>', views.contato_redirect, name='redirect'),
    path('create/', views.contato_create, name='create'),
    path('update/<int:pk>', views.contato_update, name='update'),
    path('delete/<int:pk>', views.contato_delete, name='delete')
]