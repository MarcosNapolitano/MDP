# Generated by Django 4.0.5 on 2022-06-23 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MercadoDelPlata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=60)),
                ('Cuit', models.CharField(max_length=15)),
                ('condicion', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(max_length=7),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('aclaraciones', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=200)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MercadoDelPlata.cliente')),
                ('codigo', models.ManyToManyField(to='MercadoDelPlata.producto')),
            ],
        ),
    ]
