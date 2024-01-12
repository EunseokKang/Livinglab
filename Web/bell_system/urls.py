# bell_system/urls.py

from django.urls import path
from . import views

app_name = 'bell_system'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:route_id>/', views.detail, name='detail'),
]
