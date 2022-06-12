# Generated by Django 4.0.4 on 2022-06-12 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_deparment_deparmentlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('active', models.BooleanField(default=False, verbose_name='Активный?')),
            ],
            options={
                'verbose_name': 'Подвал меню',
                'verbose_name_plural': 'Подвал меню',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='FooterList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('link', models.CharField(max_length=356, verbose_name='Ссылка')),
                ('footer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='index.footer')),
            ],
        ),
    ]