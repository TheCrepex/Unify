"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'prueba'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Saludo/', views.Saludo, name='Saludo'),
    path('Despedida/', views.Despedida, name='Despedida'),
    path('Adulto/<int:edad>/', views.Adulto, name='Adulto'),
    path('Simple/', views.Simple, name='Simple'),
    path('Dinamico/<str:name>/', views.Dinamico, name="Dinamico"),
    path('DinamicoForm/', views.DinamicoForm, name='DinamicoForm'),
    path('dinamico_view/', views.dinamico_view, name='dinamico_view'),
    path('Estaticos/', views.Estaticos, name="Estaticos"),
    path('Herencia/',views.Herencia, name= "Herencia"),
    path('Ejemplo/', views.Ejemplo, name= "Ejemplo"),
    path('Otra/', views.Otra, name= "Otra"),
]
