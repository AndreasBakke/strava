from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<club_name>/', views.weeks, name='weeks'),
    path('about/', views.about.as_view(), name='about'),
]