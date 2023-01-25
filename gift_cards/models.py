from django.db import models
from partners.models import Partner
from authentication.models import User

class GiftCard(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(verbose_name='Активна', default='True')
    partner_name = models.ForeignKey(verbose_name='Имя партнёра', to=Partner, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подарочная карта'
        verbose_name_plural = 'Подарочные карты'

class FavouriteGiftCard(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    gift_card = models.ForeignKey(GiftCard, verbose_name='Gift Card', on_delete=models.CASCADE)
