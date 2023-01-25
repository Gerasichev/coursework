from django.db import models

class Partner(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
