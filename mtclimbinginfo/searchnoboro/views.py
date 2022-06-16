from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Noboro
from .models import NoboroContent
from .forms import SearchNoboroForm
from .forms import CreateNoboroForm
from .forms import NoboroContentForm
# Create your views here.

#noboro表示
def listnoboro(request):
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

#noborocontent表示
def listnoborocontent(request, num):
    noboro = Noboro.objects.get(id=num)
    noborocontentlist = NoboroContent.objects.filter(noboro=num)
    params = {
        'title': 'NoboroContent List',
        'message': 'Noboro Content',
        #'form': ListNoboroContentForm(),
        'noboro': noboro,
        'contentlist': noborocontentlist,
    }
    #createnoboro.htmlを表示する。
    return render(request, 'searchnoboro/listnoborocontent.html', params)

#noborocontent登録
def createnoborocontent(request, num):
    if (request.method == 'POST'):
        #POSTの場合
        obj = NoboroContent()
        noborocontent = NoboroContentForm(request.POST, instance=obj)
        noborocontent.save()
        #noborocontentオブジェクトを保存後、
        #index.htmlを表示
        return redirect(to='/searchnoboro')
    params = {
        'title': 'Create NoboroContent',
        'id': num,
        'form': NoboroContentForm(),
    }
    #createnoborocontent.htmlを表示する。
    return render(request, 'searchnoboro/createnoborocontent.html', params)

def editnoborocontent(request, num):
    obj = NoboroContent.objects.get(id=num)
    if(request.method == 'POST'):
        #POSTの場合
        noborocontent = NoboroContentForm(request.POST, instance=obj)
        noborocontent.save()
        #noborocontentオブジェクトを保存後、
        #index.htmlを表示
        return redirect(to='/searchnoboro')
    params  = {
        'title': 'Edit NoboroContent',
        'id': num,
        'form': NoboroContentForm(instance=obj),
    }
    #editnoborocontent.htmlにobjを表示する。
    return render(request, 'searchnoboro/editnoborocontent.html', params)
