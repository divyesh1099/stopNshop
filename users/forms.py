from django import forms
from .models import User, Profile

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
        widget = {
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
        