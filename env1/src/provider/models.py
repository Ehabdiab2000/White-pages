from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class Provider(models.Model):
    # will contain all provider info

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User,on_delete=models.CASCADE )
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category', on_delete= models.SET_NULL, null=True)
    created = models.DateTimeField(default=timezone.now)
    service = models.CharField(max_length=100)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args , **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Provider,self).save(*args , **kwargs)

# to show the provider name in the provider list
    def __str__(self):
        return self.name


class ProviderImages(models.Model):
    # for company service category
    provider= models.ForeignKey(Provider,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Provider/',blank=True , null=True)

    #to correct the plural name
    class Meta:
        verbose_name ='provider Images'
        verbose_name_plural ='providers Images'
    def __str__(self):
        return self.provider

class Category(models.Model):
    # for company service category
    category_name= models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/',blank=True , null=True)

    #to correct the plural name
    class Meta:
        verbose_name ='category'
        verbose_name_plural ='categories'
    def __str__(self):
        return self.category_name
