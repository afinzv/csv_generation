from django import forms
from .tasks import generate
class csvform(forms.Form):
    name=forms.CharField(label='file name',min_length=4,max_length=50 ,widget=forms.TextInput(
        attrs={'class':'form control mb-3','placeholder':'File name...','id':'form-filename'}
    ))
    count=forms.IntegerField(label='number of rows',widget=forms.TextInput(
        attrs={'class':'form control mb-3','placeholder':'Enter the count...','id':'form-count'}
    ))
        