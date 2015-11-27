from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, AddCategoryForm, AddGameForm, ChangePasswordForm, Form, ImageForm, FeedbackForm, Mobile_reqForm, PlatForm, Pc_ReqForm
from .models import User, Category, Game_info, Game_request, Image, Feedback,Platform
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
import random
import string

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
            signup_success = True
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
            else:
                log_fail = True
                return render(request, 'app/login.html', {'log_fail':log_fail})

        except User.DoesNotExist:
            return redirect('app.views.user_login')

    elif request.user.is_authenticated():
        return redirect('app.views.user_home')

    return render(request, 'app/login.html', {'lst':lst})


def user_logout(request):
    logout(request)
    return redirect('app.views.user_home')

def password_change(request):
    form = ChangePasswordForm(request.POST)
    if request.method == "POST" and form.is_valid():
        new_pass = form.cleaned_data['password']
        confirm_pass = form.cleaned_data['confirm_password']
        if new_pass == confirm_pass:
            request.user.set_password(form.cleaned_data['password'])
            request.user.save()
            return redirect('app.views.user_login')
        else:
            pass_fail = True
            return render(request, 'app/changepassword.html', {'pass_fail':pass_fail})
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
        image = Image.objects.all()
        # if user is an admin
        if user.is_admin:
            return redirect('app.views.user_admin')

        # if user is not an admin.
        elif not user.is_admin:
            return render(request, 'app/home.html', {'user': user, 'lst': lst, 'games': games, 'image': image})

    if not request.user.is_authenticated():
        image = Image.objects.all()
        games = Game_info.objects.all()
        user = AnonymousUser.id
        return render(request, 'app/home.html', {'user': user, 'lst': lst, 'games': games, 'image': image})

####################### ADMIN DASHBOARD ########################

def user_admin(request):
    if request.user.is_authenticated():
        admin = User.objects.get(pk=request.user.id)
        return render(request, 'app/admin/index.html', {'user': admin})
    else:
        return redirect('app.views.user_home')

@login_required
def add_game(request):
    if request.method == "POST":
        form = AddGameForm(request.POST)
        pc = Pc_ReqForm(request.POST)
        mobile = Mobile_reqForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            model = form.save(commit=False)
            preq = pc.save()
            mreq = mobile.save()
            image = image_form.save(commit=False)
            model.pc_req = preq
            model.mobile_req = mreq
            model.save()
            image.save()
            form.save_m2m()
            game_id = Game_info.objects.get(id=model.pk)
            image.game_id = game_id
            image.save()

    else:
        form = AddGameForm()
        image_form = ImageForm()
        pc = Pc_ReqForm()
        mobile = Mobile_reqForm()
    return render(request, 'app/admin/add_game.html', {'form': form, 'image': image_form, 'pc': pc, 'mobile': mobile})

@login_required
def view_games(request):
    lists=Game_info.objects.all()
    return render(request, 'app/admin/view_games.html', {'lists': lists})

@login_required
def update_game(request, pk):
    post = get_object_or_404(Game_info, pk=pk)
    post_image = get_object_or_404(Image, game_id=pk)
    if request.method == "POST":
        form = AddGameForm(request.POST, instance=post)
        image_form = ImageForm(request.POST, request.FILES, instance=post_image)
        if form.is_valid() and image_form.is_valid():
            model = form.save(commit=False)
            image = image_form.save(commit=False)
            model.save()
            image.save()
            form.save_m2m()
            game_id = Game_info.objects.get(id=model.pk)
            image.game_id = game_id
            image.save()

    else:
        form = AddGameForm(instance=post)
        image_form = ImageForm(instance=post_image)
    return render(request, 'app/admin/add_game.html', {'form': form, 'image': image_form})    

@login_required
def delete_game(request, pk):
    lists = Game_info.objects.get(pk=pk)
    lists.is_active = False
    lists.save()
    return redirect('app.views.view_games')  

@login_required
def requested_games(request):
    if request.user.is_admin:
        return render(request, 'app/admin/requested_games.html')
    else:
        return redirect('app.views.user_home')

@login_required
def category(request):
    if request.method == "POST" and request.user.is_admin:
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('app.views.category')
    else:
        form = AddCategoryForm()
        lists = Category.objects.order_by('name').all()
    return render(request, 'app/admin/category.html', {'form': form, 'lists': lists})

@login_required
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


def request_password(request):
    if request.method == 'POST':
        subject = 'Your new password'
        message = ''.join(random.choice(string.ascii_uppercase) for i in range (6))
        from_email = request.POST['email']
        try:
            user_email = User.objects.get(email=from_email)
            send_mail(subject, message, 'nparadiang483', [from_email], fail_silently=False)
            user_email.set_password(message)
            user_email.save()
            send_success = True
            return redirect('app.views.user_login')
        except User.DoesNotExist:
            send_success = False
            return render(request, 'app/recover_password.html', {'send_success':send_success})
        

    return render(request, 'app/recover_password.html')


################################################################

def category_list(request, pk):
    lst = Category.objects.order_by('name').all()
    tlst2 = Game_info.objects.filter(category_id=pk).all()
    lst2 = []
    name = Category.objects.get(pk=pk)
    return render(request, 'app/category_list.html', {'lst':lst,'lst2':tlst2, 'name':name})

def gamepage(request, pk): # basic game page feel free to change it
    lst2 =  Game_info.objects.get(pk=pk)
    lst = Category.objects.all()
    lst3 = Feedback.objects.filter(game=pk).all()
    image = Image.objects.get(game_id=lst2)
    if request.user.is_authenticated():
        if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.game = lst2
                post.save()
        else:
            form = FeedbackForm()
        return render(request, 'app/gamepage.html', {'lst':lst,'lst2':lst2, 'form':form, 'lst3': lst3, 'image': image})
    else:
        return render(request, 'app/gamepage.html', {'lst':lst,'lst2':lst2, 'lst3': lst3, 'image': image})

@login_required
def viewreq(request):
    lists=Game_request.objects.all()
    return render(request, 'app/admin/requested.html', {'lists': lists})

@login_required
def requestgame(request, template_name='app/request.html'):
    lst = Category.objects.all()
    form2 = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            req_success = True
            return render(request, 'app/request.html', {'lst':lst, 'req_success':req_success, 'form':form2})
    else:
        form = Form()
    return render(request, template_name, {'form':form, 'lst':lst})

@login_required
def delete_request(request, pk):
    lists = Game_request.objects.get(pk=pk)
    lists.is_active = False
    lists.save()
    return redirect('app.views.viewreq')

@login_required
def platform(request):
    if request.method == "POST" and request.user.is_admin:
        form = PlatForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('app.views.platform')
    else:
        form = PlatForm()
        lists = Platform.objects.order_by('name').all()
    return render(request, 'app/admin/platform.html', {'form': form, 'lists': lists})

@login_required
def delete_platform(request, pk):
    lists = Platform.objects.get(pk=pk)
    lists.is_active = False
    lists.save()
    return redirect('app.views.platform')