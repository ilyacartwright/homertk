# Generated by Django 4.0.4 on 2022-06-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_tag_new_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
                ('position', models.SmallIntegerField(default=0, verbose_name='position')),
            ],
            options={
                'verbose_name': 'new category',
                'verbose_name_plural': 'new categories',
                'ordering': ('position',),
            },
        ),
        migrations.AddField(
            model_name='new',
            name='new_category',
            field=models.ManyToManyField(to='newsapp.newcategory', verbose_name='new categories'),
        ),
    ]