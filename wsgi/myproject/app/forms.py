from django import forms
from .models import User, Category, Game_info

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'contact_number']

        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
        }

class AddGameForm(forms.ModelForm):
	# img1 = forms.ImageField()
	# img2 = forms.ImageField()
	# img3 = forms.ImageField()
	# img4 = forms.ImageField()
	vlink = forms.CharField()
	class Meta:
		model = Game_info
		fields = ['title', 'description', 'platform', 'vlink']

class AddCategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']

