# Generated by Django 4.0.5 on 2022-06-24 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MercadoDelPlata', '0004_pruebaa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='codigo',
        ),
        migrations.AddField(
            model_name='pedido',
            name='codigo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MercadoDelPlata.producto'),
            preserve_default=False,
        ),
    ]
