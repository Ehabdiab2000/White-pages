# Generated by Django 2.2.6 on 2019-10-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0005_provider_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Provider/')),
            ],
            options={
                'verbose_name': 'provider',
                'verbose_name_plural': 'providers',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
    ]