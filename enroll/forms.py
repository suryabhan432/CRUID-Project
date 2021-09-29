from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['name','email','password']
		labels={'name':'Enter Name','email':'Enter Email','password':'Enter Password'}
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'password':forms.PasswordInput(attrs={'class':'form-control'}),
		}


class SearchStudent(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))