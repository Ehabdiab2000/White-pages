# Generated by Django 2.2.6 on 2019-11-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0010_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]