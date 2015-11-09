from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.user_add, name='user_add'),
    url(r'^login/$', views.user_login, name='user_login'),
<<<<<<< HEAD
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'adminpanel/$', views.user_admin, name='user_admin'),
    url(r'category/$', views.category, name='category'),
    url(r'^(?P<pk>[0-9]+)/deletecategory/$', views.delete_category, name='delete_category'),
    url(r'^gameinfo', views.gameinfo, name='gameinfo'),
    url(r'changepassword', views.password_change, name='changepassword'),
    url(r'', views.user_home, name='user_home'),
=======
    url(r'^home/$', views.user_home, name='user_home'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'adminpanel/$', views.user_admin, name='user_admin'),
    url(r'adminpanel/add_game/$', views.add_game, name='add_game'),
    url(r'adminpanel/update_game/$', views.update_game, name='update_game'),
    url(r'adminpanel/delete_game/$', views.delete_game, name='delete_game'),
    url(r'adminpanel/category/$', views.category, name='category'),
    url(r'adminpanel/requested_games/$', views.requested_games, name='requested_games'),
>>>>>>> 370a2976d00ba09eeb0613a76a0dd8f6c2603170
]