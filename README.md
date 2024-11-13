Price Tracking
Este proyecto es una aplicación web desarrollada con Django que permite el seguimiento y gestión de precios de commodities agrícolas, como trigo, soja, maíz y girasol. Los datos se almacenan y gestionan en una base de datos PostgreSQL. La aplicación está diseñada para mostrar los precios históricos y permitir su consulta a través de una interfaz web sencilla.


Tecnologías utilizadas
Django 5.1.2: Framework web utilizado para desarrollar la aplicación.


PostgreSQL: Sistema de gestión de bases de datos utilizado para almacenar los registros de precios de productos agrícolas.


Python 3.x: Lenguaje de programación utilizado en el desarrollo del proyecto.

psycopg2: Adaptador para conectar Django con PostgreSQL.


Instalación
Requisitos=
Asegúrate de tener los siguientes programas instalados en tu sistema:

Python 3.x

PostgreSQL (Instalado y funcionando)

pip (gestor de paquetes de Python)

Pasos para configurar el proyecto
Clona el repositorio:
bash
git clone https://github.com/Pablo1653/PriceTracking.git

Accede al directorio del proyecto:
bash
cd PriceTracking

Crea y activa un entorno virtual:

bash
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate


Instala las dependencias:

bash
pip install -r requirements.txt
Configura la base de datos PostgreSQL:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'price_tracking',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Realiza las migraciones de la base de datos:
bash
python manage.py migrate

Crea un superusuario para acceder al panel de administración:
bash
python manage.py createsuperuser

Corre el servidor de desarrollo:
bash
python manage.py runserver

Vistas del Proyecto
Este proyecto cuenta con diversas vistas para mostrar información relacionada con cultivos y precios agrícolas. Todas las vistas que requieren acceso a información privada están protegidas por autenticación, lo que garantiza que solo los usuarios autenticados puedan acceder a ellas.

Vistas de Autenticación
login_or_register: Permite a los usuarios iniciar sesión o registrarse en la aplicación.

Métodos: GET, POST

Plantilla utilizada: registration/login.html

main_view: Vista principal de la aplicación, solo accesible para usuarios autenticados.

Métodos: GET

Plantilla utilizada: prices/main.html

Vistas de Información de Cultivos
Estas vistas muestran información sobre diversos cultivos agrícolas en Argentina.

cultivos_en_argentina: Muestra información general sobre los cultivos en Argentina.

Métodos: GET

Plantilla utilizada: prices/cultivosenargentina.html

soja_cultivo: Muestra información sobre el cultivo de soja.

Métodos: GET

Plantilla utilizada: prices/soja.html

maiz_cultivo: Muestra información sobre el cultivo de maíz.

Métodos: GET

Plantilla utilizada: prices/maiz.html

girasol_cultivo: Muestra información sobre el cultivo de girasol.

Métodos: GET

Plantilla utilizada: prices/girasol.html

trigo_cultivo: Muestra información sobre el cultivo de trigo.

Métodos: GET

Plantilla utilizada: prices/trigo.html

Vistas de Precios
mostrar_precios: Muestra los precios históricos de diversos productos agrícolas.

Métodos: GET

Plantilla utilizada: prices/precios.html

Vistas de Gráficos
mostrar_grafico: Muestra un gráfico para un país y producto específico.

Métodos: GET

Plantilla utilizada: prices/graficas.html

grafico_todos_precios: Muestra un gráfico con los precios históricos de todos los productos (Maíz, Girasol, Trigo) por país. Utiliza la biblioteca matplotlib para generar los gráficos.

Métodos: GET

Plantilla utilizada: prices/graficas.html

Consideraciones
Autenticación: Todas las vistas que muestran información sensible o relevante requieren que el usuario esté autenticado a través de un inicio de sesión. Si el usuario no está autenticado, será redirigido a la página de login.

Gráficos: Los gráficos son generados utilizando la biblioteca matplotlib y se convierten a HTML con mpld3 para su visualización en la interfaz web.

Modelos de la Base de Datos
El proyecto utiliza varios modelos de Django para gestionar los datos relacionados con los precios de los productos agrícolas y las estadísticas de cultivos. A continuación, se describe la estructura de los modelos utilizados:

1. PricesTrack
Este modelo almacena información relacionada con los precios de diferentes productos agrícolas en varios países, junto con la fecha y el valor correspondiente.

python
class PricesTrack(models.Model):
    Id = models.AutoField(primary_key=True)
    Id_pais = models.SmallIntegerField()
    Pais = models.TextField()
    Producto = models.TextField()
    Fecha = models.DateField()  # Fecha en formato de fecha (DateField)
    Valor = models.BigIntegerField()

    def __str__(self):
        return f"ID: {self.Id} | País: {self.Pais} | Producto: {self.Producto} | Fecha: {self.Fecha} | Valor: {self.Valor}"
Id: Identificador único.

Id_pais: Identificador del país (pequeño entero).

Pais: Nombre del país (campo de texto).

Producto: Nombre del producto (campo de texto).

Fecha: Fecha de los precios (campo de fecha).

Valor: Valor del producto (en formato de entero grande, normalmente en miles de dólares).

2. Maiz
Este modelo almacena información sobre las estadísticas de cultivo de maíz, incluyendo detalles sobre el área sembrada, el área cosechada, la producción y el rendimiento.

python
class Maiz(models.Model):
    Id_maiz = models.AutoField(primary_key=True)
    Año = models.IntegerField()
    Provincia = models.TextField()
    Departamento = models.TextField()
    Superficie_sembrada = models.BigIntegerField(help_text="Superficie sembrada en hectáreas")
    Superficie_cosechada = models.BigIntegerField(help_text="Superficie cosechada en hectáreas")
    Produccion = models.BigIntegerField(help_text="Producción en toneladas")
    Rendimiento = models.FloatField(help_text="Rendimiento en Kg/ha")

    class Meta:
        db_table = 'maiz'

    def __str__(self):
        return f"ID: {self.Id_maiz} | Año: {self.Año} | Provincia: {self.Provincia} | Superficie sembrada: {self.Superficie_sembrada} | Producción: {self.Produccion} | Rendimiento: {self.Rendimiento}"
Año: Año del cultivo (entero).

Provincia: Provincia donde se cultivó (campo de texto).

Departamento: Departamento donde se cultivó (campo de texto).

Superficie_sembrada: Superficie sembrada en hectáreas (entero grande).

Superficie_cosechada: Superficie cosechada en hectáreas (entero grande).

Produccion: Producción total en toneladas (entero grande).

Rendimiento: Rendimiento en Kg/ha (flotante).

3. Girasol
Este modelo almacena información sobre las estadísticas de cultivo de girasol, de manera similar al modelo de maíz.

python
class Girasol(models.Model):
    Id_girasol = models.AutoField(primary_key=True)
    Año = models.IntegerField()
    Provincia = models.TextField()
    Departamento = models.TextField()
    Superficie_sembrada = models.BigIntegerField(help_text="Superficie sembrada en hectáreas")
    Superficie_cosechada = models.BigIntegerField(help_text="Superficie cosechada en hectáreas")
    Produccion = models.BigIntegerField(help_text="Producción en toneladas")
    Rendimiento = models.FloatField(help_text="Rendimiento en Kg/ha")

    class Meta:
        db_table = 'girasol'

    def __str__(self):
        return f"ID: {self.Id_girasol} | Año: {self.Año} | Provincia: {self.Provincia} | Superficie sembrada: {self.Superficie_sembrada} | Producción: {self.Produccion} | Rendimiento: {self.Rendimiento}"
Año: Año del cultivo.

Provincia: Provincia donde se cultivó.

Departamento: Departamento donde se cultivó.

Superficie_sembrada: Superficie sembrada en hectáreas.

Superficie_cosechada: Superficie cosechada en hectáreas.

Produccion: Producción en toneladas.

Rendimiento: Rendimiento en Kg/ha.

4. Soja
Este modelo almacena las estadísticas de cultivo de soja, con los mismos campos que el modelo de maíz.

python
class Soja(models.Model):
    Id_soja = models.AutoField(primary_key=True)
    Año = models.IntegerField()
    Provincia = models.TextField()
    Departamento = models.TextField()
    Superficie_sembrada = models.BigIntegerField(help_text="Superficie sembrada en hectáreas")
    Superficie_cosechada = models.BigIntegerField(help_text="Superficie cosechada en hectáreas")
    Produccion = models.BigIntegerField(help_text="Producción en toneladas")
    Rendimiento = models.FloatField(help_text="Rendimiento en Kg/ha")

    class Meta:
        db_table = 'soja'

    def __str__(self):
        return f"ID: {self.Id_soja} | Año: {self.Año} | Provincia: {self.Provincia} | Superficie sembrada: {self.Superficie_sembrada} | Producción: {self.Produccion} | Rendimiento: {self.Rendimiento}"
5. Trigo
Este modelo almacena las estadísticas de cultivo de trigo.

python
class Trigo(models.Model):
    Id_trigo = models.AutoField(primary_key=True)
    Año = models.IntegerField()
    Superficie_sembrada = models.BigIntegerField(help_text="Superficie sembrada en hectáreas")
    Superficie_cosechada = models.BigIntegerField(help_text="Superficie cosechada en hectáreas")
    Produccion = models.BigIntegerField(help_text="Producción en toneladas")
    Rendimiento = models.FloatField(help_text="Rendimiento en Kg/ha")

    class Meta:
        db_table = 'trigo'

    def __str__(self):
        return f"ID: {self.Id_trigo} | Año: {self.Año} | Superficie sembrada: {self.Superficie_sembrada} | Superficie cosechada: {self.Superficie_cosechada} | Producción: {self.Produccion} | Rendimiento: {self.Rendimiento}"
Año: Año del cultivo.

Superficie_sembrada: Superficie sembrada en hectáreas.

Superficie_cosechada: Superficie cosechada en hectáreas.

Produccion: Producción en toneladas.

Rendimiento: Rendimiento en Kg/ha.

Notas
Cada modelo tiene un campo __str__ para representar sus instancias de manera legible.

Los modelos de cultivos (Maiz, Girasol, Soja, Trigo) tienen campos relacionados con las superficies sembrada y cosechada, la producción y el rendimiento en cada año y región.

Se han utilizado tipos de datos como IntegerField, BigIntegerField, y FloatField para representar de manera eficiente los valores en la base de datos.

Licencia

Desarrollado íntegramente por Ing. agr Sanguinetti Flores, Pablo Maria.

