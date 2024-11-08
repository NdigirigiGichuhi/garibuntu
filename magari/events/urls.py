from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:event_id>/register', views.register_for_event, name='register_for_event'),
]