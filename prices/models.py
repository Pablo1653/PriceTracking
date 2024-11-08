from django.db import models

class PricesTrack(models.Model):
    Id = models.AutoField(primary_key=True)
    Id_pais = models.SmallIntegerField()
    Pais = models.TextField()  
    Producto = models.TextField()
    Fecha = models.IntegerField()  
    Valor = models.BigIntegerField()

    def __str__(self):
        return f"ID: {self.Id} | Id_pais: {self.Id_pais} | Pais: {self.Pais} | Producto: {self.Producto} | Fecha: {self.Fecha} | Valor: {self.Valor}"


class Maiz(models.Model):
    Id_maiz = models.AutoField(primary_key=True)
    Año_maiz = models.IntegerField()
    Provincia_maiz = models.TextField()
    Departamento_maiz = models.TextField()
    Superficie_sembrada_maiz = models.BigIntegerField(help_text="Superficie sembrada en hectáreas")
    Superficie_cosechada_maiz = models.BigIntegerField(help_text="Superficie cosechada en hectáreas")
    Produccion_maiz = models.BigIntegerField(help_text="Producción en toneladas")
    Rendimiento_maiz = models.FloatField(help_text="Rendimiento en Kg/ha")

    class Meta:
        db_table = 'maiz'

    def __str__(self):
        return f"ID: {self.Id_maiz} | Año: {self.Año_maiz} | Provincia: {self.Provincia_maiz} | Departamento: {self.Departamento_maiz} | Superficie sembrada: {self.Superficie_sembrada_maiz} | Superficie cosechada: {self.Superficie_cosechada_maiz} | Producción: {self.Produccion_maiz} | Rendimiento: {self.Rendimiento_maiz}"


class Girasol(models.Model):
    Id_girasol = models.AutoField(primary_key=True)
    Año_girasol = models.IntegerField()
    Provincia_girasol = models.TextField()
    Departamento_girasol = models.TextField()
    Superficie_sembrada_girasol = models.BigIntegerField(help_text="Superficie sembrada en hectáreas")
    Superficie_cosechada_girasol = models.BigIntegerField(help_text="Superficie cosechada en hectáreas")
    Produccion_girasol = models.BigIntegerField(help_text="Producción en toneladas")
    Rendimiento_girasol = models.FloatField(help_text="Rendimiento en Kg/ha")

    class Meta:
        db_table = 'girasol'

    def __str__(self):
        return f"ID: {self.Id_girasol} | Año: {self.Año_girasol} | Provincia: {self.Provincia_girasol} | Departamento: {self.Departamento_girasol} | Superficie sembrada: {self.Superficie_sembrada_girasol} | Superficie cosechada: {self.Superficie_cosechada_girasol} | Producción: {self.Produccion_girasol} | Rendimiento: {self.Rendimiento_girasol}"


class Soja(models.Model):
    Id_soja = models.AutoField(primary_key=True)
    Año_soja = models.IntegerField()
    Provincia_soja = models.TextField()
    Departamento_soja = models.TextField()
    Superficie_sembrada_soja = models.BigIntegerField(help_text="Superficie sembrada en hectáreas")
    Superficie_cosechada_soja = models.BigIntegerField(help_text="Superficie cosechada en hectáreas")
    Produccion_soja = models.BigIntegerField(help_text="Producción en toneladas")
    Rendimiento_soja = models.FloatField(help_text="Rendimiento en Kg/ha")

    class Meta:
        db_table = 'soja'

    def __str__(self):
        return f"ID: {self.Id_soja} | Año: {self.Año_soja} | Provincia: {self.Provincia_soja} | Departamento: {self.Departamento_soja} | Superficie sembrada: {self.Superficie_sembrada_soja} | Superficie cosechada: {self.Superficie_cosechada_soja} | Producción: {self.Produccion_soja} | Rendimiento: {self.Rendimiento_soja}"



class Trigo(models.Model):
    Id_trigo = models.AutoField(primary_key=True)
    Año_trigo = models.IntegerField()
    Superficie_sembrada_trigo = models.BigIntegerField(help_text="Superficie sembrada en hectáreas")
    Superficie_cosechada_trigo = models.BigIntegerField(help_text="Superficie cosechada en hectáreas")
    Produccion_trigo = models.BigIntegerField(help_text="Producción en toneladas")
    Rendimiento_trigo = models.FloatField(help_text="Rendimiento en Kg/ha")

    class Meta:
        db_table = 'trigo'

    def __str__(self):
        return f"ID: {self.Id_trigo} | Año: {self.Año_trigo} | Superficie sembrada: {self.Superficie_sembrada_trigo} | Superficie cosechada: {self.Superficie_cosechada_trigo} | Producción: {self.Produccion_trigo} | Rendimiento: {self.Rendimiento_trigo}"
