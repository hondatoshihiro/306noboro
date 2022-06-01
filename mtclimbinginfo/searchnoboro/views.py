from django.shortcuts import render
from django.http import HttpResponse
from .models import Noboro
from .forms import SearchNoboroForm
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
