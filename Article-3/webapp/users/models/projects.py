from tkinter.tix import Balloon
from django.db import models
from uuid import uuid4

from .users import User

class ProgrammingLanguage(models.Model):
   id = models.UUIDField(unique=True, default=uuid4, editable=False, primary_key=True)
   title = models.CharField(max_length=150)
   version = models.CharField(max_length=100)
   updated_at = models.DateTimeField(auto_now=True)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.title


class Project(models.Model):
   _id = models.UUIDField(unique=True, primary_key=True, default=uuid4, editable=False)
   title = models.CharField(max_length=150)
   owner = models.OneToOneField(User, on_delete=models.CASCADE, related_query_name="project" )
   language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE, related_name="projects")
   contributors = models.ManyToManyField(User, related_name="project_contributors")
   updated_at = models.DateTimeField(auto_now=True)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.title