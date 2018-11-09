from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.listar),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
