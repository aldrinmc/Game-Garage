from django import forms
from .models import Category, Game_info, Game_request, Image, User, Feedback, Platform, PC_requirement, Mobile_requirement
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
    category_id = forms.ModelMultipleChoiceField(label = "Category", queryset=Category.objects.filter(is_active=True).order_by('name').all(), widget=forms.CheckboxSelectMultiple)
    platform = forms.ModelMultipleChoiceField(label = "Platform", queryset=Platform.objects.filter(is_active=True).order_by('name').all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Game_info
        fields = [
            'title', 'description', 'platform', 'category_id', 'redirectlink', 'youtubelink'
        ]

        redirectlink = forms.CharField(widget=forms.URLInput)
        youtubelink = forms.CharField(widget=forms.URLInput)
        widgets = {
            'redirectlink': forms.URLInput(),
            'youtubelink': forms.URLInput(),
        }


class CategoryForm(forms.ModelForm):
    categorylist = forms.ModelMultipleChoiceField(queryset=Category.objects.filter(is_active=True).all(), to_field_name='category')

class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password', 'confirm_password']

        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }

class Form(forms.ModelForm):
    class Meta:
        model = Game_request
        fields = ['title']

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['thumbnail', 'img1', 'img2', 'img3', 'img4']
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'rating' ]

class PlatForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name']

class Pc_ReqForm(forms.ModelForm):
    class Meta:
        model = PC_requirement
        fields = ['os_min', 'processor_min', 'memory_min', 'graphics_min', 'directx_min', 'harddrive_min', 'os_rec', 'processor_rec', 'memory_rec', 'graphics_rec', 'directx_rec', 'harddrive_rec']

class Mobile_reqForm(forms.ModelForm):
    class Meta:
        model = Mobile_requirement
        fields = ['compatible']