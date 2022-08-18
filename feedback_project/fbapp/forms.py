from django import forms

class FbForm(forms.Form):
	name = forms.CharField()
	feedback = forms.CharField(widget=forms.Textarea(attrs={ 'rows' : 4, 'cols' : 40}))
	