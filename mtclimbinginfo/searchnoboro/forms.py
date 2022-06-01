from django import forms

class SearchNoboroForm(forms.Form):
    id = forms.IntegerField(label='ID')
    #volno = forms.IntegerField(label='volno')
    #year = forms.IntegerField(label='year')
    #season = forms.CharField(label='season')
