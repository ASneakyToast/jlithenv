from django.urls import path

from . import views


app_name = 'portfolio'
urlpatterns = [
    path('', views.portfolio_index, name='index'),
    path('<strip_title>/', views.strip_page, name='section'),
]
