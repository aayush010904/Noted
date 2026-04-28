from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/welcome.html'

class AuthorisedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorised.html'
    login_url = '/admin'



# def home(request):
#     return render(request, 'home/welcome.html')

# @login_required(login_url='/admin')
# def authorize(request):
#     return render(request, 'home/authorized.html')