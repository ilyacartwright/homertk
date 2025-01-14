# Generated by Django 4.0.4 on 2022-06-11 23:08

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_companygoal_options_companygoal_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('body', ckeditor.fields.RichTextField(max_length=900, verbose_name='Текст')),
                ('show_list', models.BooleanField(default=False, verbose_name='Показывать список?')),
                ('active', models.BooleanField(default=False, verbose_name='Активный?')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='DeparmentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('punkt', models.CharField(max_length=256, verbose_name='Пункт списка')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='index.department')),
            ],
            options={
                'verbose_name': 'Список',
                'verbose_name_plural': 'Список',
            },
        ),
    ]
