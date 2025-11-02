from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mailing.urls')),  # ← Перенаправляем корень на приложение
    path('users/', include('users.urls')),
]
