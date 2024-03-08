# Generated by Django 5.0.3 on 2024-03-07 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViaCepModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.IntegerField(verbose_name='Cep do usuário')),
                ('logradouro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Logradouro')),
                ('complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro')),
                ('localidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Localidade')),
                ('uf', models.CharField(blank=True, max_length=100, null=True, verbose_name='UF')),
            ],
        ),
    ]