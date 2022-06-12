# Generated by Django 4.0.4 on 2022-06-12 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deparment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('body', models.TextField(max_length=9000, verbose_name='Текст')),
                ('show_list', models.BooleanField(default=False, verbose_name='Показывать список?')),
                ('active', models.BooleanField(default=False, verbose_name='Активный?')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='DeparmentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punkt', models.CharField(max_length=256, verbose_name='Пункт списка')),
                ('deparment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='index.deparment')),
            ],
            options={
                'verbose_name': 'Список',
                'verbose_name_plural': 'Список',
            },
        ),
    ]
