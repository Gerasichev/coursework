# Generated by Django 4.1.1 on 2022-10-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0002_alter_discount_partner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='address',
            field=models.CharField(default='exit', max_length=500, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discount',
            name='metro',
            field=models.CharField(default='exit', max_length=255, verbose_name='Метро'),
            preserve_default=False,
        ),
    ]
