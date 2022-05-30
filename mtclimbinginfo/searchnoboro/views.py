from django.shortcuts import render
from django.http import HttpResponse
from .models import Noboro

# Create your views here.

def index(request):
    data = Noboro.objects.all()
    params = {
        'title': 'Search Noboro',
        'message': 'all Noboros.',
        'data': data,
    }
    return render(request, 'searchnoboro/index.html', params)
