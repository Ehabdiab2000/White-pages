# Generated by Django 2.2.6 on 2019-10-20 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0006_auto_20191020_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='providerimages',
            options={'verbose_name': 'provider Images', 'verbose_name_plural': 'providers Images'},
        ),
        migrations.AlterField(
            model_name='providerimages',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.Provider'),
        ),
    ]
