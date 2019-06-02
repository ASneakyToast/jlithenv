from django.urls import path

from . import views


app_name = 'portfolio'
urlpatterns = [
    path('', views.table_of_contents, name='index'),
    path('<section_title>/', views.section_page, name='section'),
]
