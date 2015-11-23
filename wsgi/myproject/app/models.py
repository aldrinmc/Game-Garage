from datetime import time
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# CUSTOM USER AUTH
###############################################################################

class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email,
            is_superuser=True,
            is_staff=True,
            is_active=True,
            is_admin=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return UserManager

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    contact_number = models.CharField(max_length=30, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email

    objects = UserManager()

###############################################################################
###############################################################################
###############################################################################

class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    return 'uploads/' + get_random_string(length=25) + '.' + ext


class Game_info(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=3000)
    category_id = models.ManyToManyField(Category)
    platform = models.CharField(max_length=50)
    redirectlink = models.CharField(max_length=250, null=True, blank=True)
    youtubelink = models.CharField(max_length=250, null=True, blank=True)
    os_min = models.CharField(max_length=50, default = "", null=True, blank=True)
    processor_min = models.CharField(max_length=50, default = "", null=True, blank=True)
    memory_min = models.CharField(max_length=50, default = "", null=True, blank=True)
    graphics_min = models.CharField(max_length=50, default = "", null=True, blank=True)
    directx_min = models.CharField(max_length=50, default = "", null=True, blank=True)
    harddrive_min = models.CharField(max_length=50, default = "", null=True, blank=True)
    os_rec = models.CharField(max_length=50, default = "", null=True, blank=True)
    processor_rec = models.CharField(max_length=50, default = "", null=True, blank=True)
    memory_rec = models.CharField(max_length=50, default = "", null=True, blank=True)
    graphics_rec = models.CharField(max_length=50, default = "", null=True, blank=True)
    directx_rec = models.CharField(max_length=50, default = "", null=True, blank=True)
    harddrive_rec = models.CharField(max_length=50, default = "", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    thumbnail = models.ImageField(upload_to=generate_filename)
    img1 = models.ImageField(upload_to=generate_filename)
    img2 = models.ImageField(upload_to=generate_filename)
    img3 = models.ImageField(upload_to=generate_filename)
    img4 = models.ImageField(upload_to=generate_filename)
    game_id = models.ForeignKey(Game_info, null=True, blank=True)



class Feedback(models.Model):
    comment = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    rating = models.IntegerField()
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game_info, default=1)
    is_active = models.BooleanField(default=True)

class Game_request(models.Model):
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()
