from django.urls import path
from . import views

urlpatterns = [
    #searchnoboro app内のurlを記載(http://localhost:8000/searchnoboro/～)
    path('', views.index, name='index'),
    path('createnoboro', views.createnoboro, name='createnoboro'),
    path('editnoboro/<int:num>', views.editnoboro, name='editnoboro'),
    path('deletenoboro/<int:num>', views.deletenoboro, name='deletenoboro'),
    path('listnoborocontent/<int:num>', views.listnoborocontent, name='listnoborocontent'),
]
