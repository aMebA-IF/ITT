# Generated by Django 3.1.7 on 2021-05-14 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PlacesRemember', '0002_auto_20210513_1712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=25, max_digits=30, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=25, max_digits=30, null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlacesRemember.profile', unique=True),
        ),
    ]
