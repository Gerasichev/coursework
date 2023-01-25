# Generated by Django 4.1.1 on 2022-09-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('partner_name', models.CharField(max_length=255, verbose_name='Имя партнёра')),
                ('start_date', models.DateTimeField(verbose_name='Начало действия')),
                ('expire_date', models.DateTimeField(verbose_name='Действует до:')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
    ]