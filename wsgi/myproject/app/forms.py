from django import forms
from .models import Category, Game_info, Game_request, Image, User, Feedback, Platform, System_requirement
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
    tchoices = ((0,"0-Stars"),(1,"1-Stars"),(2,"2-Stars"),(3,"3-Stars"),(4,"4-Stars"),(5,"5-Stars"))
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=tchoices)
    class Meta:
        model = Feedback
        fields = ['comment', 'rating' ]

class PlatForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name']

class System_ReqForm(forms.ModelForm):
    processor_min = forms.CharField(label='Processor Minimum ')
    memory_min =    forms.CharField(label='Memory Minimum    ')
    graphics_min =  forms.CharField(label='Graphics Minimum  ')
    storage_min = forms.CharField(label='Storage Minimum')
    processor_rec = forms.CharField(label='Processor Recommended ')
    memory_rec =    forms.CharField(label='Memory Recommended    ')
    graphics_rec =  forms.CharField(label='Graphics Recommended  ')
    storage_rec = forms.CharField(label='Storage Recommended')
    class Meta:
        model = System_requirement
        fields = ['processor_min', 'memory_min', 'graphics_min', 
            'storage_min', 'processor_rec', 'memory_rec', 'graphics_rec',  
            'storage_rec'
        ]
