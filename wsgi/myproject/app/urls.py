from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.user_add, name='user_add'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^home/$', views.user_home, name='user_home'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'adminpanel/$', views.user_admin, name='user_admin'),
]