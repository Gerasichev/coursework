from tkinter import CASCADE
from django.db import models
from partners.models import Partner

class Discount(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    partner_name = models.ForeignKey(verbose_name='Имя партнёра', to=Partner, on_delete=models.CASCADE)
    start_date = models.DateTimeField(verbose_name='Начало действия')
    expire_date = models.DateTimeField(verbose_name='Действует до:')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


    