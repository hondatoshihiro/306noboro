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
    params = {
        'title': 'Search Noboro',
        'form': CreateNoboroForm(),
    }
    if (request.method == 'POST'):
        volno = request.POST['volno']
        year = request.POST['year']
        season = request.POST['season']
        noboro = Noboro(volno = volno, year = year, season = season)
        noboro.save()
        return redirect(to='/searchnoboro')
    return render(request, 'searchnoboro/createnoboro.html', params)
