from django.contrib import admin
from .models.users import User
from .models.projects import ProgrammingLanguage, Project


admin.site.register((ProgrammingLanguage,Project, User))
