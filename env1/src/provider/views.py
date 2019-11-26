from django.shortcuts import render
from .models import Provider , ProviderImages ,Category
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

def providerlist(request,category_slug = None):
    category = None
    providerlist = Provider.objects.all()
    categorylist = Category.objects.annotate(total_providers=Count('provider'))

    if category_slug:
        category= get_object_or_404(Category, slug = category_slug)
        providerlist = Category.filter(category=category)
    search_query = request.GET.get('q')
    if search_query :
        providerlist = providerlist.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)|
            Q(category__category__name__icontains  = search_query))

    template = 'provider/provider_list.html'

    context = {'provider_list': providerlist ,'category_list' : categorylist}

    return  render(request,template,context)


def providerdetail(request,provider_slug):
    #print(provider_slug)
    providerdetail=get_object_or_404(Provider,slug=provider_slug)
    providerimage =  ProviderImages.objects.filter(provider = providerdetail)
    template ='provider/provider_detail.html'
    context = {'provider_detail': providerdetail, 'provider_image' : providerimage}
    return render(request, template, context)