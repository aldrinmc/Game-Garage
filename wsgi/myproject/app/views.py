from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, AddCategoryForm, AddGameForm, ChangePasswordForm, Form
from .models import User, Category, Game_info, Game_request
from django.http import Http404
from app import admin

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'app/login.html')

    if request.user.is_authenticated():
        return redirect('app.views.user_home')


#######################USER###############################################################
#######################USER###############################################################
#######################USER###############################################################
def user_add(request):
    lst = Category.objects.all()
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
        return render(request, 'app/signup.html', {'form': form, 'lst':lst})

    return render(request, 'app/signup.html', {'form': form, 'lst':lst})


def user_login(request):
    lst = Category.objects.all()
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

    return render(request, 'app/login.html', {'lst':lst})


def user_logout(request):
    logout(request)
    return redirect('app.views.user_login')

def password_change(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            post = User.objects.get(password=form.old_password)
            post.set_password(form.password)
            post.save()
            return redirect('app.views.user_login')
    else:
        form = ChangePasswordForm()
    return render(request, 'app/changepassword.html', {'form': form})

# if successfully log in, this function is called.
# the user is either admin or not admin
# different view for admin and not admin
def user_home(request):
    lst = Category.objects.all()
    if request.user.is_authenticated():
        user = User.objects.get(pk=request.user.id)
        games = Game_info.objects.all()

        # if user is an admin
        if user.is_admin:
            return redirect('app.views.user_admin')

        # if user is not an admin.
        elif not user.is_admin:
            return render(request, 'app/home.html', {'user': user, 'games': games, 'lst':lst})

    if not request.user.is_authenticated():
        return redirect('app.views.user_login')

####################### ADMIN DASHBOARD ########################

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

def update_game(request):
    return render(request, 'app/admin/update_game.html')
    
def delete_game(request):
    return render(request, 'app/admin/delete_game.html')

def requested_games(request):
    return render(request, 'app/admin/requested_games.html')

def category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('app.views.category')
    else:
        form = AddCategoryForm()
        lists = Category.objects.all()
    return render(request, 'app/admin/category.html', {'form': form, 'lists': lists})

def delete_category(request, pk):
    lists = Category.objects.get(pk=pk)
    lists.is_active = False
    lists.save()
    return redirect('app.views.category')

def gameinfo(request):
    lst = Category.objects.all()
    if request.method == "POST":
        form = AddGameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category_id = Category.objects.get(pk=1)
            post.save()
            return redirect('app.views.user_admin')
    else:
        form = AddGameForm()
    return render(request, 'app/admin/gameinfo.html', {'form': form, 'lst':lst})

################################################################

def category_list(request, pk):
    lst = Category.objects.all()
    tlst2 = Game_info.objects.all()
    lst2 = []
    name = Category.objects.get(pk=pk).name
    for i in range(len(tlst2)):
        if(name == tlst2[i].category_id.name):
            lst2.append(tlst2[i])
    return render(request, 'app/category_list.html', {'lst':lst,'lst2':lst2, 'name':name})

def gamepage(request, pk): # basic game page feel free to change it
    lst2 =  Game_info.objects.get(pk=pk)
    lst = Category.objects.all()
    return render(request, 'app/gamepage.html', {'lst':lst,'lst2':lst2})

def viewreq(request):
    lists=Game_request.objects.all()
    return render(request, 'app/admin/requested.html', {'lists': lists})


def requestgame(request ,template_name ='app/request.html'):
    form = Form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('app.views.user_admin')
    return render(request, template_name, {'form':form})
    
def delete_request(request, pk):
    lists = Game_request.objects.get(pk=pk)
    lists.is_active = False
    lists.save()
    return redirect('app.views.viewreq')
