# Generated by Django 5.1.2 on 2024-10-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PricesTrack',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Id_pais', models.SmallIntegerField()),
                ('Pais', models.TextField()),
                ('Producto', models.TextField()),
                ('Fecha', models.IntegerField()),
                ('Valor', models.BigIntegerField()),
            ],
        ),
    ]
