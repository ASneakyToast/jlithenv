from django.contrib import admin
from django.urls import path, include

from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('portfolio/', include('portfolio.urls')),
]

urlpatterns += staticfiles_urlpatterns()
