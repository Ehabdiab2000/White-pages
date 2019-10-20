from django.shortcuts import render
from .models import Provider
# Create your views here.

def providerlist(request):
    providerlist = Provider.objects.all()
    template = 'Provider/provider_list.html'

    context = {'provider_list': providerlist}

    return  render(request,template,context)


def providerdetail(request,provider_slug):
    print(provider_slug)
    providerdetail=Provider.get(slug=provider_slug)
    template ='provider/provider_detail.html'
    context = {'provider_detail': providerdetail}
    return render(request, template, context)