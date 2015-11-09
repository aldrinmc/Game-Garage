from django import forms
from .models import User, Category, Game_info, Game_request
from django.forms import ModelForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'contact_number']

        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class AddGameForm(forms.ModelForm):
    class Meta:
        model = Game_info
        fields = ['title', 'description', 'platform', 'category_id', 'img', 'thumbnail', 'dlink', 'vlink', 'is_active']

class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['old_password', 'password', 'confirm_password']

        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'old_password': forms.PasswordInput(),
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }

class Form(ModelForm):
    class Meta:
        model = Game_request
        fields = ['title']