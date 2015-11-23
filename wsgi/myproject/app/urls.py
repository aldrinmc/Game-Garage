from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'category/$', views.category, name='category'),
    url(r'^register/$', views.user_add, name='user_add'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'adminpanel/$', views.user_admin, name='user_admin'),
    url(r'adminpanel/add_game/$', views.add_game, name='add_game'),
    url(r'adminpanel/viewgames/$', views.view_games, name='view_games'),
    url(r'adminpanel/update_game/(?P<pk>[0-9]+)/$', views.update_game, name='update_game'),
    url(r'^(?P<pk>[0-9]+)/adminpanel/delete_game/$', views.delete_game, name='delete_game'),
    url(r'^(?P<pk>[0-9]+)/delete_category/$', views.delete_category, name='delete_category'),
    url(r'^gameinfo', views.gameinfo, name='gameinfo'),
    url(r'^(?P<pk>[0-9]+)/category_list/$', views.category_list, name='category_list'),
    url(r'^(?P<pk>[0-9]+)/gamepage/$', views.gamepage, name='gamepage'),
    url(r'changepassword', views.password_change, name='changepassword'),
    url(r'request', views.requestgame, name='request'),
    url(r'^viewreq/$',views.viewreq, name='viewreq'),
    url(r'^(?P<pk>[0-9]+)/delete_req/$',views.delete_request, name='delete_req'),
    url(r'^recover_password/$',views.request_password, name='request_password'),
    url(r'', views.user_home, name='user_home'),
]
