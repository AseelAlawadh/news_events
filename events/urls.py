from django.urls import path, include
from . import views


urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:event_id>', views.detail, name='detail'),
    path('<int:event_id>/coming', views.coming, name='coming'),


]