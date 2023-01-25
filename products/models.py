from django.db import models
from partners.models import Partner

class Product(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=255)
    partner_name = models.ForeignKey(verbose_name='Имя партнёра', to=Partner, on_delete=models.CASCADE)
    is_discount = models.BooleanField(verbose_name='Действует скдика', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

