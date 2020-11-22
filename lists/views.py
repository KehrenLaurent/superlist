from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from lists.models import Item, List
from lists.forms import ItemForm
# Create your views here.


def home_page(request):
    return render(request, 'lists/home.html', {'form': ItemForm()})


def view_list(request, pk):
    list_ = List.objects.get(pk=pk)
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
    return render(request, 'lists/list.html', {'form': form, 'list': list_})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(list=list_, text=request.POST['text'])
        return redirect(list_)
    else:
        return render(request, 'lists/home.html', {'form': form})
