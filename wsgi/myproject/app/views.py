from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .models import User
from django.http import Http404


def index(request):
    if not request.user.is_authenticated():
        return HttpResponse("please login")

    if request.user.is_authenticated():
        return HttpResponse("you already login!")


#######################USER###############################################################
#######################USER###############################################################
#######################USER###############################################################
def user_add(request):
    try:
        if request.method == 'POST':

            fname = request.POST['fname']
            lname = request.POST['lname']
            contact_number = request.POST['contact_number']
            email = request.POST['email']
            password = request.POST['password']

            user = User.objects.create_user(email=email, password=password)
            user.first_name = fname
            user.last_name = lname
            user.contact_number = contact_number
            user.save()
            return redirect('app.views.user_login')

        else:
            form = UserForm()
    except:
        form = UserForm()
        return render(request, 'app/signup.html', {'form': form})

    return render(request, 'app/signup.html', {'form': form})
