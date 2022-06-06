from tempfile import template
from django.urls import path
from .views import UserView, CustomTemplateView
from django.views.generic import TemplateView

urlpatterns = [
   path('user/', UserView.as_view(), name='users'),
   path('templates/', TemplateView.as_view(template_name="general/index.html"), name='templates'),
   path('view/', CustomTemplateView.as_view(), name='templates'),

]