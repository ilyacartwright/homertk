from django.db import models
from ckeditor.fields import RichTextField


    

class CompanyGoal(models.Model):
    title = models.CharField('Название', max_length=256)
    img_class = models.CharField('Класс иконки', max_length=256)
    body = models.CharField('Текст', max_length=900)
    active = models.BooleanField('Активный?', default=False)

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = "Деятельность"
        ordering = ['-pk']


class Department(models.Model):
    title = models.CharField('Название', max_length=256)
    body = RichTextField('Текст', max_length=900)
    show_list = models.BooleanField('Показывать список?', default=False)
    active = models.BooleanField('Активный?', default=False)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = "Отделы"

class DeparmentList(models.Model):
    department = models.ForeignKey('Department', on_delete=models.PROTECT, blank=True, null=True)
    punkt = models.CharField('Пункт списка', max_length=256)

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = "Список"
