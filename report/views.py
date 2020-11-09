from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def report(request):
    form = reportIssue()

    if request.method == 'POST':
        form = reportIssue(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/reportIssue")

    context = {'form':form}
    return render(request, 'report/report.html', context)