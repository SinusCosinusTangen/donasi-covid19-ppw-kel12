from django.shortcuts import render, redirect
from .forms import FormPendonor
from .models import Pendonor

def donate(request):
    form = FormPendonor(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, 'main/donate.html', context)