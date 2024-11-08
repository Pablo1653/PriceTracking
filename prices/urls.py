from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Ruta para la vista principal
    path('', views.main_view, name='main_view'),
    path('cultivosenargentina/', views.cultivos_en_argentina, name='cultivosenargentina'),
    path('precios/', views.mostrar_precios, name='mostrar_precios'),
    path('soja/', views.soja_cultivo, name='soja_cultivo'),
    path('maiz/', views.maiz_cultivo, name='maiz_cultivo'),
    path('girasol/', views.girasol_cultivo, name='girasol_cultivo'),
    path('trigo/', views.trigo_cultivo, name='trigo_cultivo'),
    path("grafico-todos/", views.grafico_todos_precios, name="grafico_todos_precios"),

    # Ruta para login y registro
    path('login/', views.login_or_register, name='login_or_register'),

    # Logout
    path('logout/', LogoutView.as_view(), name='logout'),
]
