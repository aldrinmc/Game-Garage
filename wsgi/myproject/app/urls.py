from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.user_add, name='user_add'),
    url(r'^login/$', views.user_login, name='user_login'),
]