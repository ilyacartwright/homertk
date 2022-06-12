from django.db import models

class CompanyGoal(models.Model):
    title = models.CharField('Название', max_length=256)
    img_class = models.CharField('Класс иконки', max_length=256)
    body = models.CharField('Текст', max_length=900)
    active = models.BooleanField('Активный?', default=False)

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = "Деятельность"
        ordering = ['-pk']