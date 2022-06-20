from django.urls import path
from . import views

urlpatterns = [
    #searchnoboro app内のurlを記載(http://localhost:8000/searchnoboro/～)
    #path('', views.index, name='index'),
    path('', views.listnoboro, name='index'),
    path('listnoborocontent/<int:num>', views.listnoborocontent, name='listnoborocontent'),
    path('createnoboro', views.createnoboro, name='createnoboro'),
    path('createnoborocontent/<int:num>', views.createnoborocontent, name='createnoborocontent'),
    path('editnoboro/<int:num>', views.editnoboro, name='editnoboro'),
    path('editnoborocontent/<int:num>', views.editnoborocontent, name='editnoborocontent'),
    path('deletenoboro/<int:num>', views.deletenoboro, name='deletenoboro'),
    path('deletenoborocontent/<int:num>', views.deletenoborocontent, name='deletenoborocontent'),
]
