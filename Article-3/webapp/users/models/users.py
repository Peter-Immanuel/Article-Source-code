from typing import List
from uuid import uuid4
from django.db import models
from django.contrib.auth.base_user import (
   AbstractBaseUser, BaseUserManager
)
from django.utils.translation import gettext_lazy as _

from webapp.utils.constants import GENDER




class UserManager(BaseUserManager):
   """ Custom user model manager with unique identifier as email """

   def create_user(self, email, password, **extra_fields):
      ''' Create and save a user with the given email and password. '''
      if not email:
         raise ValueError('Email must be provided.')
      email = self.normalize_email(email)
      user = self.model(email=email, **extra_fields)
      user.set_password(password)
      user.save(using=self._db)
      return user

   def create_superuser(self, email, password, **extra_fields):
      ''' Create and save a superuser with the given email and password. '''
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)
      extra_fields.setdefault('is_active', True)

      if extra_fields.get('is_superuser') is not True:
         raise ValueError(_('Superuser must have is_superuser=True.'))
      if extra_fields.get('is_staff') is not True:
         raise ValueError(_('Superuser must have is_staff=True.'))
      return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser):
   _id = models.UUIDField(unique=True, default=uuid4, editable=False)
   email = models.EmailField(unique=True, verbose_name="email address")
   password = models.CharField(max_length=128, verbose_name="password")
   geek_name = models.CharField(max_length=40)
   gender = models.CharField(max_length=7, choices=GENDER, default="Gender")  
   github_profile = models.CharField(max_length=255, null=True)
   date_of_birth = models.DateField()
   country = models.CharField(max_length=150, blank=True)
   is_active = models.BooleanField(default=False)
   is_staff = models.BooleanField(default=False)
   is_superuser = models.BooleanField(default=False)  
   updated_at = models.DateTimeField(auto_now=True)
   created_at = models.DateTimeField(auto_now_add=True, editable=False)

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS: List[str] = ["geek_name",]

   objects = UserManager()

   def __str__(self) -> str:
      ''' Returns geek_name as representation of the User object '''
      return self.geek_name

   def get_full_name(self):
      ''' Returns full name of the User object '''
      return f"{self.first_name} {self.last_name}"

   def get_email(self):
      ''' Returns email of the User object '''
      return self.email

   



