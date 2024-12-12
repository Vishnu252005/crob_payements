from django import forms
from directory.models import Profile

class AccountProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('name','email', 'profile_pic','phone_num', 'college_name', 'branch', 'year')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
			'profile_pic': forms.FileInput(attrs={'class': 'form-control'}), 
			'phone_num': forms.TextInput(attrs={'class': 'form-control'}),
			'college_name': forms.TextInput(attrs={'class': 'form-control'}),
			'branch': forms.TextInput(attrs={'class': 'form-control'}),
			'year': forms.TextInput(attrs={'class': 'form-control'}),
		}
