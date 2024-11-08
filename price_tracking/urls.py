from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Agrega esta línea



urlpatterns = [
    # Redirige la ruta raíz a login si no estás autenticado
    path('', lambda request: redirect('login_or_register'), name='home'),  # Esto redirige a login_or_register

    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),

    # Ruta para las URLs de autenticación proporcionadas por Django (login, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Ruta para incluir las URLs de la aplicación 'prices'
    path('prices/', include('prices.urls')),
]
