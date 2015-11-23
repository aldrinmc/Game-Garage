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
    category_id = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Game_info
        fields = ['title', 'description', 'platform', 'category_id', 'redirectlink', 'youtubelink']


class CategoryForm(forms.ModelForm):
    categorylist = forms.ModelMultipleChoiceField(queryset=Category, to_field_name='category')

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
