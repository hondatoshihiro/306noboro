from django import forms

from .models import Noboro
from .models import NoboroContent

#index.htmlに表示する項目
class SearchNoboroForm(forms.Form):
    id = forms.IntegerField(label='ID')
    #volno = forms.IntegerField(label='volno')
    #year = forms.IntegerField(label='year')
    #season = forms.CharField(label='season')

class CreateNoboroForm(forms.Form):
    #Formの仕組み modelとは関係なく、項目を定義する
    volno = forms.IntegerField(label='volno', widget=forms.NumberInput(attrs={'class':'form-control'}))
    year = forms.IntegerField(label='year', widget=forms.NumberInput(attrs={'class':'form-control'}))
    season = forms.CharField(label='season', widget=forms.TextInput(attrs={'class':'form-control'}))

class CreateNoboroForm(forms.ModelForm):
    #ModelFormの仕組み、この文法なに？
    class Meta:
        model = Noboro
        fields = ['volno', 'year', 'season']

class NoboroContentForm(forms.ModelForm):
    #ModelFormの仕組み、この文法なに？
    class Meta:
        model = NoboroContent
        fields = ['title', 'subtitle', 'pageno', 'content']

