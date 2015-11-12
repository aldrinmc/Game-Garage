from django import forms
from .models import Category, Game_info, Game_request, Image, User
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
        fields = ['title', 'description', 'platform','rlink','vlink','category_id']


class CategoryForm(forms.ModelForm):
    categorylist = forms.ModelMultipleChoiceField(queryset=Category, to_field_name='category')

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