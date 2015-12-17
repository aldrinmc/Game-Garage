from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, AddCategoryForm, AddGameForm, ChangePasswordForm, Form, ImageForm, FeedbackForm, PlatForm, \
    System_ReqForm
from .models import User, Category, Game_info, Game_request, Image, Feedback, Platform, System_requirement
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
import random
import string


#######################USER###############################################################
#######################USER###############################################################
#######################USER###############################################################
def user_add(request):
    games = Game_info.objects.filter(is_active=True).all()
    lst = Category.objects.filter(is_active=True).all()
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
            return render(request, 'app/signup.html', {'signup_success': signup_success, 'lst': lst, 'games': games})

        else:
            form = UserForm()
    except:
        form = UserForm()
        return render(request, 'app/signup.html', {'form': form, 'lst': lst, 'games': games})

    return render(request, 'app/signup.html', {'form': form, 'lst': lst, 'games': games})


def user_login(request):
    lst = Category.objects.filter(is_active=True).all()
    games = Game_info.objects.filter(is_active=True).all()
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
                return render(request, 'app/login.html', {'log_fail': log_fail, 'games': games})

        except User.DoesNotExist:
            return redirect('app.views.user_login')

    elif request.user.is_authenticated():
        return redirect('app.views.user_home')

    return render(request, 'app/login.html', {'lst': lst, 'games': games})

def user_logout(request):
    logout(request)
    return redirect('app.views.user_home')


def password_change(request):
    lst = Category.objects.filter(is_active=True).all()
    games = Game_info.objects.filter(is_active=True).all()
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
            return render(request, 'app/changepassword.html', {'pass_fail': pass_fail, 'lst': lst, 'games': games})
    else:
        form = ChangePasswordForm()
    return render(request, 'app/changepassword.html', {'form': form, 'lst': lst, 'games': games})


# if successfully log in, this function is called.
# the user is either admin or not admin
# different view for admin and not admin
def user_home(request):
    lst = Category.objects.filter(is_active=True).all()
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
    if request.user.is_authenticated() and request.user.is_admin:
        admin = User.objects.get(pk=request.user.id)
        return render(request, 'app/admin/index.html', {'user': admin})
    else:
        return redirect('app.views.user_home')


@login_required
def add_game(request):
    if request.user.is_admin:
        if request.method == "POST":
            form = AddGameForm(request.POST)
            sys = System_ReqForm(request.POST)
            image_form = ImageForm(request.POST, request.FILES)
            if form.is_valid() and image_form.is_valid():
                model = form.save(commit=False)
                image = image_form.save(commit=False)
                sysreq = sys.save(commit=False)
                model.is_active = True
                model.save()
                image.save()
                form.save_m2m()
                game_id = Game_info.objects.get(id=model.pk)
                sysreq.gameinfo_id = game_id
                sysreq.save()
                image.game_id = game_id
                image.save()
                return redirect('app.views.view_games')
            else:
                gamelist = Game_info.objects.all()
                for i in gamelist:
                    if i.title == request.POST['title']:
                        return redirect('app.views.update_game', i.id)
        else:
            form = AddGameForm()
            image_form = ImageForm()
            sys = System_ReqForm()
        return render(request, 'app/admin/add_game.html', {'form': form, 'image': image_form, 'sys': sys})
    else:
        return redirect('app.views.user_home')


@login_required
def view_games(request):
    if request.user.is_admin:
        lists = Game_info.objects.filter(is_active=True).all()
        return render(request, 'app/admin/view_games.html', {'lists': lists})
    else:
        return redirect('app.views.user_home')


@login_required
def update_game(request, pk):
    if request.user.is_admin:
        post = get_object_or_404(Game_info, pk=pk)
        post_sys = System_requirement.objects.filter(gameinfo_id=pk)[
            len(System_requirement.objects.filter(gameinfo_id=pk)) - 1]
        post_image = get_object_or_404(Image, game_id=pk)
        deleted = post.is_active
        if request.method == "POST":
            form = AddGameForm(request.POST, instance=post)
            sys = System_ReqForm(request.POST)
            image_form = ImageForm(request.POST, request.FILES, instance=post_image)
            if form.is_valid() and image_form.is_valid():
                model = form.save(commit=False)
                image = image_form.save(commit=False)
                sysreq = sys.save(commit=False)
                sysreq.save()
                model.is_active = True
                model.save()
                image.save()
                form.save_m2m()
                game_id = Game_info.objects.get(id=model.pk)
                sysreq.gameinfo_id = game_id
                sysreq.save()
                image.game_id = game_id
                image.save()
                return redirect('app.views.view_games')
        else:
            form = AddGameForm(instance=post)
            sys = System_ReqForm(instance=post_sys)
            image_form = ImageForm(instance=post_image)
        return render(request, 'app/admin/add_game.html',
                      {'form': form, 'sys': sys, 'image': image_form, 'deleted': deleted})
    else:
        return redirect('app.views.user_home')


@login_required
def add_requested(request, pk):
    if request.user.is_admin:
        post = get_object_or_404(Game_request, pk=pk)
        if request.method == 'POST':
            form = AddGameForm(request.POST)
            sys = System_ReqForm(request.POST)
            image_form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                model = form.save(commit=False)
                image = image_form.save(commit=False)
                sysreq = sys.save(commit=False)
                model.is_active = True
                model.save()
                image.save()
                form.save_m2m()
                game_id = Game_info.objects.get(id=model.pk)
                sysreq.gameinfo_id = game_id
                sysreq.save()
                image.game_id = game_id
                image.save()
                return redirect('app.views.view_games')
            else:
                gamelist = Game_info.objects.all()
                for i in gamelist:
                    if i.title == request.POST['title']:
                        return redirect('app.views.update_game', i.id)
        else:
            form = AddGameForm(instance=post)
            sys = System_ReqForm()
            image_form = ImageForm()
        return render(request, 'app/admin/add_game.html', {'form': form, 'sys': sys, 'image': image_form})
    else:
        return redirect('app.views.user_home')


@login_required
def delete_game(request, pk):
    if request.user.is_admin:
        lists = Game_info.objects.get(pk=pk)
        lists.is_active = False
        lists.save()
        return redirect('app.views.view_games')
    else:
        return redirect('app.views.user_home')


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
    elif request.user.is_admin:
        form = AddCategoryForm()
        lists = Category.objects.order_by('name').all()
    return render(request, 'app/admin/category.html', {'form': form, 'lists': lists})


@login_required
def delete_category(request, pk):
    if request.user.is_admin:
        lists = Category.objects.get(pk=pk)
        lists.is_active = False
        lists.save()
        return redirect('app.views.category')
    else:
        return redirect('app.views.user_home')


def gameinfo(request):
    lst = Category.objects.filter(is_active=True).all()
    games = Game_info.objects.filter(is_active=True).all()
    if request.method == "POST":
        form = AddGameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category_id = Category.objects.get(pk=1)
            post.save()
            return redirect('app.views.user_admin')
    else:
        form = AddGameForm()
        return render(request, 'app/admin/gameinfo.html', {'form': form, 'lst': lst, 'games': games})


def request_password(request):
    if request.method == 'POST':
        subject = 'Your new password'
        message = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
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
            return render(request, 'app/recover_password.html', {'send_success': send_success})

    return render(request, 'app/recover_password.html')


################################################################

def category_list(request, pk):
    games = Game_info.objects.filter(is_active=True).all()
    lst = Category.objects.filter(is_active=True).order_by('name').all()
    tlst2 = Game_info.objects.filter(category_id=pk).filter(is_active=True).all()
    image = Image.objects.all()
    name = Category.objects.get(pk=pk)
    return render(request, 'app/category_list.html',
                  {'lst': lst, 'lst2': tlst2, 'name': name, 'image': image, 'games': games})


def gamepage(request, pk):
    lst2 = Game_info.objects.get(pk=pk)
    games = Game_info.objects.filter(is_active=True).all()
    lst = Category.objects.filter(is_active=True).all()
    lst3 = Feedback.objects.filter(game=pk).all()
    sysreq = System_requirement.objects.filter(gameinfo_id=pk)[
        len(System_requirement.objects.filter(gameinfo_id=pk)) - 1]
    image = Image.objects.get(game_id=lst2)
    plat = lst2.platform.all()
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
        return render(request, 'app/gamepage.html',
                      {'lst': lst, 'lst2': lst2, 'form': form, 'lst3': lst3, 'sysreq': sysreq, 'plat': plat,
                       'image': image, 'games': games})
    else:
        return render(request, 'app/gamepage.html',
                      {'lst': lst, 'lst2': lst2, 'lst3': lst3, 'sysreq': sysreq, 'plat': plat, 'image': image,
                       'games': games})


@login_required
def viewreq(request):
    if request.user.is_admin:
        lists = Game_request.objects.all()
        return render(request, 'app/admin/requested.html', {'lists': lists})
    else:
        return redirect('app.views.user_home')


@login_required
def requestgame(request, template_name='app/request.html'):
    lst = Category.objects.filter(is_active=True).all()
    form2 = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            req_success = True
            return render(request, 'app/request.html', {'lst': lst, 'req_success': req_success, 'form': form2})
    else:
        form = Form()
    return render(request, template_name, {'form': form, 'lst': lst})


@login_required
def delete_request(request, pk):
    if request.user.is_admin:
        lists = Game_request.objects.get(pk=pk)
        lists.is_active = False
        lists.save()
        return redirect('app.views.viewreq')
    else:
        return redirect('app.views.user_home')


@login_required
def platform(request):
    if request.method == "POST" and request.user.is_admin:
        form = PlatForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('app.views.platform')
    elif request.user.is_admin:
        form = PlatForm()
        lists = Platform.objects.order_by('name').all()
    return render(request, 'app/admin/platform.html', {'form': form, 'lists': lists})


@login_required
def delete_platform(request, pk):
    if request.user.is_admin:
        lists = Platform.objects.get(pk=pk)
        lists.is_active = False
        lists.save()
        return redirect('app.views.platform')
    else:
        return redirect('app.views.user_home')


def about_us(request):
    lst = Category.objects.filter(is_active=True).all()
    games = Game_info.objects.filter(is_active=True).all()
    return render(request, 'app/about.html', {'lst': lst, 'games': games})


def searchgame_name(request):
    if request.method == "GET":
        search_name = request.GET.get('game_name')
        gamename = Game_info.objects.filter(title__istartswith=search_name)
        allgame = Game_info.objects.filter(is_active=True).all()
        lst = Category.objects.filter(is_active=True).order_by('name').all()
        return render(request, 'app/searchgame_page.html',
                    {'gamename': gamename, 'lst': lst, 'search_name': search_name, 'games': allgame})


def succ_pass(request):
    games = Game_info.objects.filter(is_active=True).all()
    lst = Category.objects.filter(is_active=True).all()
    return render(request, 'app/changepass_succ.html', {'lst': lst, 'games': games})
