from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_record/', views.add_record, name='add_record'),
]
