from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Noboro
from .models import NoboroContent
from .forms import SearchNoboroForm
from .forms import CreateNoboroForm
# Create your views here.

#noboro表示
def index(request):
    params = {
        'title': 'Search Noboro',
        'message': 'all Noboros.',
        'form': SearchNoboroForm(),
        'data': [],
    }
    if (request.method == 'POST'):
        #POSTの場合
        num=request.POST['id']
        item = Noboro.objects.get(id=num)
        params['data'] = [item]
        params['form'] = SearchNoboroForm(request.POST)
    else:
        #POSTではない場合
        params['data'] = Noboro.objects.all()
    #index.htmlにparamsを渡して表示
    return render(request, 'searchnoboro/index.html', params)

#noboro登録
def createnoboro(request):
    if (request.method == 'POST'):
        #POSTの場合
        obj = Noboro()
        noboro = CreateNoboroForm(request.POST, instance=obj)
        noboro.save()
        #noboroオブジェクトを保存後、
        #index.htmlを表示
        return redirect(to='/searchnoboro')
    params = {
        'title': 'Create Noboro',
        'form': CreateNoboroForm(),
    }
    #createnoboro.htmlを表示する。
    return render(request, 'searchnoboro/createnoboro.html', params)

#noboro編集
def editnoboro(request, num):
    obj = Noboro.objects.get(id=num)
    if(request.method == 'POST'):
        #POSTの場合
        noboro = CreateNoboroForm(request.POST, instance=obj)
        noboro.save()
        #noboroオブジェクトを保存後、
        #index.htmlを表示
        return redirect(to='/searchnoboro')
    params  = {
        'title': 'Edit Noboro',
        'id': num,
        'form': CreateNoboroForm(instance=obj),
    }
    #editnoboro.htmlにobjを表示する。
    return render(request, 'searchnoboro/editnoboro.html', params)

#noboro削除
def deletenoboro(request, num):
    noboro = Noboro.objects.get(id=num)
    if(request.method == 'POST'):
        noboro.delete()
        #noboroオブジェクトを削除後、
        #index.htmlを表示
        return redirect(to='/searchnoboro')
    params = {
        'title': 'Delete Noboro',
        'id': num,
        'obj': noboro,
    }
    #deletenoboro.htmlにnoboroを表示する。
    return render(request, 'searchnoboro/deletenoboro.html', params)

#content表示
def listnoborocontent(request, num):
    #noborocontentlist = NoboroContent.objects.get_queryset(noboro=num)
    noborocontentlist = NoboroContent.objects.filter(noboro=num)
    params = {
        'title': 'NoboroContent List',
        'message': 'Noboro Content',
        #'form': ListNoboroContentForm(),
        'data': noborocontentlist,
    }
    #createnoboro.htmlを表示する。
    return render(request, 'searchnoboro/listnoborocontent.html', params)
