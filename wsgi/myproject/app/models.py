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
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

class Game_info(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=3000)
    platform = models.CharField(max_length=15)
    category_id = models.ForeignKey(Category)
    img = models.ImageField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    dlink = models.CharField(max_length=100, null=True, blank=True)
    vlink = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    comment = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    rating = models.IntegerField()
    user = models.ForeignKey(User)
    is_active = models.BooleanField(default=True)

class Game_request(models.Model):
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User)
    is_active = models.BooleanField(default=True)
