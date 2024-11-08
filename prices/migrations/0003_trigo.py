# Generated by Django 5.1.2 on 2024-10-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_girasol_maiz_soja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trigo',
            fields=[
                ('Id_trigo', models.AutoField(primary_key=True, serialize=False)),
                ('Año_trigo', models.IntegerField()),
                ('Superficie_sembrada_trigo', models.BigIntegerField(help_text='Superficie sembrada en hectáreas')),
                ('Superficie_cosechada_trigo', models.BigIntegerField(help_text='Superficie cosechada en hectáreas')),
                ('Produccion_trigo', models.BigIntegerField(help_text='Producción en toneladas')),
                ('Rendimiento_trigo', models.FloatField(help_text='Rendimiento en Kg/ha')),
            ],
            options={
                'db_table': 'trigo',
            },
        ),
    ]
