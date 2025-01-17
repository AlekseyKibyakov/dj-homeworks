from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as f:
        stations = list(csv.DictReader(f))
    paginator = Paginator(stations, 10)
    page_num = int(request.GET.get('page', '1'))
    page = paginator.get_page(page_num)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
