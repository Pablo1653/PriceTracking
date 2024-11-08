import matplotlib
matplotlib.use('Agg')  # Usa el backend 'Agg' para evitar problemas de GUI
import matplotlib.pyplot as plt
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import PricesTrack, Maiz, Trigo, Soja, Girasol
import mpld3
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, LoginForm  # Asegúrate de importar ambos formularios
from django.contrib import messages  # Importa para mostrar mensajes de error

# Vista principal que requiere autenticación
@login_required
def main_view(request):
    return render(request, 'prices/main.html')


# Vista de login y registro
# Vista de login y registro
def login_or_register(request):
    form_login = AuthenticationForm()
    form_register = CustomUserCreationForm()
    action = request.GET.get('action', 'login')  # Acción por defecto 'login'

    if request.method == "POST":
        if action == 'login':
            form_login = AuthenticationForm(request, data=request.POST)
            if form_login.is_valid():
                username = form_login.cleaned_data['username']
                password = form_login.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Has iniciado sesión correctamente.")
                    return redirect('main_view')  # Redirige al main_view después de iniciar sesión
                else:
                    messages.error(request, "Contraseña incorrecta. Por favor, intenta nuevamente.")
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        
        elif action == 'register':
            form_register = CustomUserCreationForm(request.POST)
            if form_register.is_valid():
                form_register.save()
                messages.success(request, "Usuario registrado con éxito. Ahora puedes iniciar sesión.")
                return redirect('login_or_register')  # Redirige al login después del registro

    return render(request, 'registration/login.html', {
        'form_login': form_login,
        'form_register': form_register,
        'action': action  # Variable para controlar qué formulario mostrar
    })
# Otras vistas que requieren autenticación
@login_required
def cultivos_en_argentina(request):
    return render(request, 'prices/cultivosenargentina.html')

@login_required
def mostrar_precios(request):
    registros = PricesTrack.objects.all()
    return render(request, 'prices/precios.html', {'records': registros})

@login_required
def soja_cultivo(request):
    registros = Soja.objects.all()
    return render(request, 'prices/soja.html', {'records': registros})

@login_required
def maiz_cultivo(request):
    registros = Maiz.objects.all()
    return render(request, 'prices/maiz.html', {'records': registros})

@login_required
def girasol_cultivo(request):
    registros = Girasol.objects.all()
    return render(request, 'prices/girasol.html', {'records': registros})

@login_required
def trigo_cultivo(request):
    registros = Trigo.objects.all()
    return render(request, 'prices/trigo.html', {'records': registros})

@login_required
def mostrar_grafico(request, pais, producto):
    context = {
        "pais": pais,
        "producto": producto,
    }
    return render(request, 'prices/graficas.html', context)

@login_required
def grafico_todos_precios(request):
    datos = PricesTrack.objects.all().values("Fecha", "Valor", "Pais", "Producto")
    df = pd.DataFrame(datos)  # Convierte el queryset a un DataFrame

    if df.empty:
        return HttpResponse("No hay datos disponibles para graficar.", content_type="text/plain")

    fig, ax = plt.subplots(figsize=(12, 8))  # Aumenta el tamaño del gráfico

    colores = {
        'Maiz': 'green',
        'Girasol': 'yellow',
        'Trigo': 'blue',
    }

    for (producto, pais), grupo in df.groupby(["Producto", "Pais"]):
        line, = ax.plot(grupo["Fecha"], grupo["Valor"], marker='o', color=colores.get(producto, 'gray'),
                        label=f"{producto} - {pais}", linewidth=2)
        
        tooltip = mpld3.plugins.PointLabelTooltip(line, labels=[f"{producto} - {pais}\nValor: {val}" for val in grupo["Valor"]])
        mpld3.plugins.connect(fig, tooltip)

    ax.set_title("Precios históricos por cultivo y país", fontsize=16)
    ax.set_xlabel("Fecha", fontsize=14)
    ax.set_ylabel("Valor (cientos de USD)", fontsize=14)
    ax.grid(True)
    ax.tick_params(axis='both', labelsize=12)  # Aumenta el tamaño de las etiquetas
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje X

    plt.figtext(0.5, 0, 'Referencia: FAOSTAT, Crops and livestock products, Food and agriculture database',
                wrap=True, horizontalalignment='center', fontsize=12)

    graph_html = mpld3.fig_to_html(fig)
    plt.close()

    return render(request, 'prices/graficas.html', {'graph_html': graph_html})
