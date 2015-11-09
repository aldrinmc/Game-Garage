from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.user_add, name='user_add'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'adminpanel/$', views.user_admin, name='user_admin'),
    url(r'category/$', views.category, name='category'),
    url(r'^(?P<pk>[0-9]+)/deletecategory/$', views.delete_category, name='delete_category'),
    url(r'^gameinfo', views.gameinfo, name='gameinfo'),
    url(r'changepassword', views.password_change, name='changepassword'),
    url(r'', views.user_home, name='user_home'),
]