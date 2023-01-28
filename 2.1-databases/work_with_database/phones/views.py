from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_order = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort_order == 'name':
        phones = phones.order_by('name')
    elif sort_order == 'min_price':
        phones = phones.order_by('price')
    elif sort_order == 'max_price':
        phones = phones.order_by('-price')
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context=context)
