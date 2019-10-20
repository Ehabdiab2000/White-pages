from django.contrib import admin

# Register your models here.
from .models import Provider, Category ,ProviderImages
admin.site.register(Provider)
admin.site.register(Category)
admin.site.register(ProviderImages)