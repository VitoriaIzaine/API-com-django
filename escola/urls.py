from django.contrib import admin
from django.urls import path, include
from cursos import views

urlpatterns = [
    path('',views.index,name='home'),
    path('api/v1/',include('cursos.urls')),
    path('auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
