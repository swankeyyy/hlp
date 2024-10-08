# Generated by Django 5.0.4 on 2024-06-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название соцсети')),
                ('icon', models.CharField(max_length=100, verbose_name='Font Awesome Icon')),
                ('link', models.TextField(verbose_name='Адрес ссылки')),
            ],
        ),
    ]
