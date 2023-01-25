# Generated by Django 4.1.1 on 2022-09-23 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_active', models.BooleanField(default='True', verbose_name='Активна')),
                ('partner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.partner', verbose_name='Имя партнёра')),
            ],
            options={
                'verbose_name': 'Подарочная карта',
                'verbose_name_plural': 'Подарочные карты',
            },
        ),
    ]