from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<club_name>/', views.weeks, name='weeks'),
    path(r'^about/$', views.about, name='about'),
]