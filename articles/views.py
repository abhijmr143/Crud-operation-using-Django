from django.shortcuts import render
from .models import Articles
from django.shortcuts import get_object_or_404
from .forms import ArticleForm
from django.http import HttpResponseRedirect


# Create your views here.


def index(request):
    data = Articles.objects.all()
    return render(request, 'articles/index.html', {'data': data})


def detail(request, id):
    data = get_object_or_404(Articles, id=id)
    return render(request, 'articles/detail.html', {'data': data})


def create(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return HttpResponseRedirect('/')
    return render(request, 'articles/create.html', {'form': form})


def update(request, id):
    data = get_object_or_404(Articles, id=id)
    form = ArticleForm(request.POST or None, instance=data)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'articles/update.html', {'form': form})


def delete(request, id):
    conext = {}
    data = get_object_or_404(Articles, id=id)
    if request.method == 'POST':
        data.delete()
        return HttpResponseRedirect('/')
    return render(request, 'articles/delete.html', conext)