from django.shortcuts import render, redirect
from . forms import contactForm
from . import models


# Create your views here.
def home(request):
    return render(request, 'home.html') 

def form(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request, 'form.html', {'form':form}) 

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name' : name, 'email': email, 'select' : select})
    else:
        return render(request, 'about.html')


# Create your views here.
def model(request):
    student = models.Student.objects.all()
    return render(request,"model.html", {'data': student})

def delete_student(request, roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect("model")