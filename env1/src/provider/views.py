from django.shortcuts import render
from .models import Provider , ProviderImages ,Category
from django.db.models import Count

# Create your views here.

def providerlist(request):
    providerlist = Provider.objects.all()
    categorylist = Category.objects.annotate(total_providers=Count('provider'))
    template = 'provider/provider_list.html'

    context = {'provider_list': providerlist ,'category_list' : categorylist}

    return  render(request,template,context)


def providerdetail(request,provider_slug):
    #print(provider_slug)
    providerdetail=Provider.GET(slug=provider_slug)
    providerimage =  ProviderImages.object.filter(provider = providerdetail)
    template ='provider/provider_detail.html'
    context = {'provider_detail': providerdetail, 'productimage' : providerimage}
    return render(request, template, context)