from django.urls import path
from . import views
app_name = 'provider'
urlpatterns =[
    path('', views.providerlist , name='provider_list'),
    path ('<slug:provider_slug>',views.providerdetail, name='provider_detail')
]