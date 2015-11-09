from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, AddGameForm, AddCategoryForm
from .models import User, Game_info
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

def user_login(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('app.views.user_home')

        except User.DoesNotExist:
            return redirect('app.views.user_login') 

    elif request.user.is_authenticated():
        return redirect('app.views.user_home')

    return render(request, 'app/login.html')   

def user_home(request):
    if request.user.is_authenticated():
        user = User.objects.get(pk=request.user.id)

        # if user is an admin
        if user.is_admin:
            return redirect('app.views.user_admin')

        # if user is not an admin.
        elif not user.is_admin:
            return render(request, 'app/home.html', {'user': user})

    if not request.user.is_authenticated():
        return redirect('app.views.user_login')


def user_logout(request):
    logout(request)
    return redirect('app.views.user_login')

#################### ADMIN DASHBOARD #######################

def user_admin(request):
    if request.user.is_authenticated():
        admin = User.objects.get(pk=request.user.id)
        return render(request, 'app/admin/index.html', {'user': admin})
    else:
        return redirect('app.views.user_login')

def add_game(request):
    if request.method == "POST":
        form = AddGameForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.save() 
    else:
        form = AddGameForm()
    return render(request, 'app/admin/add_game.html', {'form': form})

def update_game(request, pk):
    return render(request, 'app/update_game.html', {'form': form})

def delete_game(request):
    return render(request, 'app/admin/delete_game.html')

def category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.save() 
    else:
        form = AddCategoryForm()
    return render(request, 'app/admin/add_category.html', {'form': form})

def requested_games(request):
    return render(request, 'app/admin/requested_games.html')

#############################################################