from django import forms

class SearchNoboroForm(forms.Form):
    id = forms.IntegerField(label='ID')
    #volno = forms.IntegerField(label='volno')
    #year = forms.IntegerField(label='year')
    #season = forms.CharField(label='season')

class CreateNoboroForm(forms.Form):
    volno = forms.IntegerField(label='volno', widget=forms.NumberInput(attrs={'class':'form-control'}))
    year = forms.IntegerField(label='year', widget=forms.NumberInput(attrs={'class':'form-control'}))
    season = forms.CharField(label='season', widget=forms.TextInput(attrs={'class':'form-control'}))
    