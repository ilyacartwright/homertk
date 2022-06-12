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

class Deparment(models.Model):
    title = models.CharField('Название', max_length=256)
    body = models.TextField('Текст', max_length=9000)
    show_list = models.BooleanField('Показывать список?', default=False)
    active = models.BooleanField('Активный?', default=False)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = "Отделы"

class DeparmentList(models.Model):
    deparment = models.ForeignKey('Deparment', on_delete=models.PROTECT, blank=True, null=True)
    punkt = models.CharField('Пункт списка', max_length=256)

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = "Список"

class Footer(models.Model):
    title = models.CharField('Название', max_length=256)
    active = models.BooleanField('Активный?', default=False)

    class Meta:
        verbose_name = 'Подвал меню'
        verbose_name_plural = "Подвал меню"

class FooterList(models.Model):
    title = models.CharField('Название', max_length=256)
    link = models.CharField('Ссылка', max_length=356)
    footer = models.ForeignKey('Footer', on_delete=models.PROTECT, blank=True, null=True)