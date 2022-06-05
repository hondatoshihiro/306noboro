from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Noboro
from .forms import SearchNoboroForm
from .forms import CreateNoboroForm
# Create your views here.

def index(request):
    params = {
        'title': 'Search Noboro',
        'message': 'all Noboros.',
        'form': SearchNoboroForm(),
        'data': [],
    }
    if (request.method == 'POST'):
        num=request.POST['id']
        item = Noboro.objects.get(id=num)
        params['data'] = [item]
        params['form'] = SearchNoboroForm(request.POST)
    else:
        params['data'] = Noboro.objects.all()
    return render(request, 'searchnoboro/index.html', params)

def createnoboro(request):
    if (request.method == 'POST'):
        obj = Noboro()
        noboro = CreateNoboroForm(request.POST, instance=obj)
        noboro.save()
        return redirect(to='/searchnoboro')
    params = {
        'title': 'Create Noboro',
        'form': CreateNoboroForm(),
    }
    return render(request, 'searchnoboro/createnoboro.html', params)

def editnoboro(request, num):
    obj = Noboro.objects.get(id=num)
    if(request.method == 'POST'):
        noboro = CreateNoboroForm(request.POST, instance=obj)
        noboro.save()
        return redirect(to='/searchnoboro')
    params  = {
        'title': 'Edit Noboro',
        'id': num,
        'form': CreateNoboroForm(instance=obj),
    }
    return render(request, 'searchnoboro/editnoboro.html', params)

