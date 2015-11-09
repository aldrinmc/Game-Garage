from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.user_add, name='user_add'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^home/$', views.user_home, name='user_home'),
    url(r'adminpanel/$', views.user_admin, name='user_admin'),
    url(r'adminpanel/add_game/$', views.add_game, name='add_game'),
    url(r'adminpanel/update_game/$', views.update_game, name='update_game'),
    url(r'adminpanel/delete_game/$', views.delete_game, name='delete_game'),
    url(r'adminpanel/requested_games/$', views.requested_games, name='requested_games'),
    url(r'category/$', views.category, name='category'),
    url(r'^(?P<pk>[0-9]+)/deletecategory/$', views.delete_category, name='delete_category'),
    url(r'^gameinfo', views.gameinfo, name='gameinfo'),
    url(r'^(?P<pk>[0-9]+)/category_list/$', views.category_list, name='category_list'),
    url(r'^(?P<pk>[0-9]+)/gamepage/$', views.gamepage, name='gamepage'),
    url(r'changepassword', views.password_change, name='changepassword'),
]