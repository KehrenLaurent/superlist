from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.


def home_page(request):
    return render(request, 'lists/home.html')


def view_list(request, pk):
    list_ = List.objects.get(pk=pk)
    error = None

    if request.method == 'POST':
        try:
            item = Item.objects.create(
                text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect('/lists/{}/'.format(list_.id))
        except ValidationError:
            error = "You can't have an empty list item"
    return render(request, 'lists/list.html', {'list': list_, 'error': error})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(
        text=request.POST.get('item_text', ''), list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'lists/home.html', {'error': error})
    return redirect('/lists/{}/'.format(list_.pk))
