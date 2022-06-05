from django.urls import path
from . import views

urlpatterns = [
    #searchnoboro app内のurlを記載(http://localhost:8000/searchnoboro/～)
    path('', views.index, name='index'),
    path('createnoboro', views.createnoboro, name='createnoboro'),
]