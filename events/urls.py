from django.urls import path, include
from . import views


urlpatterns = [
    path('create_event', views.create_event, name='create_event'),
    path('<int:event_id>', views.detail_event, name='detail_event'),
    path('<int:event_id>/coming', views.coming, name='coming'),


]