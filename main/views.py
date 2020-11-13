from django.shortcuts import render, redirect
from .form import QuestionForm

def home(request):
    form = QuestionForm()

    if request.method == "POST" :
        if request.POST.get("ask") :
            form = QuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("pertanyaan:pertanyaan")
        if request.POST.get("seeAll") :
            return redirect("pertanyaan:pertanyaan")
    context = {
        'form' : form
    }
    return render(request, 'main/home.html', context)
