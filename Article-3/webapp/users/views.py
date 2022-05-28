from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.

from .forms import UserForm

class UserView(View):
   template_name = 'user/user.html'
   form = UserForm

   def get(self, request):
      form = self.form()
      return render(request, self.template_name, {'form': form})

   def post(self, request):
      form = self.form(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponse("Success!!!")
      return render(request, self.template_name, {'form': form})


