from django.contrib import admin
from django.urls import path
from consumo_universitario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('calcular_huella/', views.calcular_huella, name='calcular')
]
