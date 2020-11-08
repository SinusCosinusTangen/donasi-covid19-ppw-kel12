from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# Create your views here.
def daftarDonasi(request):
    pendonor = Pendonor.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(pendonor, 10)

    try:
        donasi = paginator.page(page)
    except PageNotAnInteger:
        donasi = paginator.page(1)
    except EmptyPage:
        donasi = paginator.page(paginator.num_pages)

    return render(request, 'daftarDonasi/daftarDonasi.html', {'donasi':donasi})