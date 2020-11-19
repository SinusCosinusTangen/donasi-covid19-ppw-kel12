from donasi.forms import FormLembaga
from django.shortcuts import render, redirect
from .models import Donasi

# Create your views here.
def institutionReg(request):
    form = FormLembaga()
    context = {'form':form}
    if request.method == "POST": 
        form = FormLembaga(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect('/institution')

    return render(request, 'donasi/donasi.html', context)

def seeInstitution(request):
    institution = Donasi.objects.all()
    context = {'institution':institution}

    return render(request, 'donasi/lihat.html', context)