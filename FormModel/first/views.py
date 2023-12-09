from django.shortcuts import render
from .forms import MyForm
from .models import BlogPost

def index(request):
    return render(request, 'base.html')
def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = MyForm()

    return render(request, 'form.html', {'form': form})


def blog_post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'model.html', {'posts': posts})

