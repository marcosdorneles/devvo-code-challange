# Generated by Django 5.1.7 on 2025-03-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('poder', models.CharField(max_length=100)),
                ('portador', models.CharField(max_length=100)),
                ('forjadoPor', models.CharField(max_length=100)),
                ('imagem', models.URLField()),
            ],
        ),
    ]
