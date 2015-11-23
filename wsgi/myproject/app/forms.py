from django import forms
from .models import Category, Game_info, Game_request, Image, User, Feedback
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
    category_id = forms.ModelMultipleChoiceField(label = "Category", queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    os_min =        forms.CharField(label='OS Minimum        ')
    processor_min = forms.CharField(label='Processor Minimum ')
    memory_min =    forms.CharField(label='Memory Minimum    ')
    graphics_min =  forms.CharField(label='Graphics Minimum  ')
    directx_min =   forms.CharField(label='DirectX Minimum   ')
    harddrive_min = forms.CharField(label='Hard Drive Minimum')
    os_rec =        forms.CharField(label='OS Recommended        ')
    processor_rec = forms.CharField(label='Processor Recommended ')
    memory_rec =    forms.CharField(label='Memory Recommended    ')
    graphics_rec =  forms.CharField(label='Graphics Recommended  ')
    directx_rec =   forms.CharField(label='DirectX Recommended   ')
    harddrive_rec = forms.CharField(label='Hard Drive Recommended')
    class Meta:
        model = Game_info
        fields = [
            'title', 'description', 'platform', 'category_id', 'redirectlink', 'youtubelink',
            'os_min', 'processor_min', 'memory_min', 'graphics_min', 'directx_min', 'harddrive_min',
            'os_rec', 'processor_rec', 'memory_rec', 'graphics_rec', 'directx_rec', 'harddrive_rec'
        ]


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