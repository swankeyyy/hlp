# Generated by Django 5.0.4 on 2024-05-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog.tag', verbose_name='Теги'),
        ),
    ]
