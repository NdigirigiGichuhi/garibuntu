from django.urls import path, include
from . import views
app_name = 'garibuntu'
urlpatterns = [
    path('', views.home, name='home'),
    path('users/', include('users.urls', namespace='users')), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cargroupslist/', views.car_group_list, name='car_group_list'), 
    path('car-groups/<int:group_id>/', views.car_group_detail, name='car_group_detail'),
    path('even-list/', views.event_list, name='event_list'),
    path('car-group/', views.group_list_dash, name='group_list_dash'),
    path('master-register', views.master_register, name='master_register'),
]