# Generated by Django 4.1.7 on 2023-04-01 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('short_url', models.CharField(blank=True, db_index=True, max_length=10, unique=True, verbose_name='Сокращение')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
    ]