from django.urls import path
from mailing import views

urlpatterns = [
    path('', views.home, name='home'),
    # Добавьте другие маршруты для рассылок
]
