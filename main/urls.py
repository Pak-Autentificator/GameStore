from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('sell/', views.sell, name="sell"),
    path('test/', views.test, name='test'),




]