from typing import Any
from django.db import models
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import EditUserForm, ProfilePageForm
from weblog.models import Profile
# Create your views here.

class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_user_profile.html'
    
    form_class = ProfilePageForm
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_user_profile.html'
    fields =['bio','profile_pic']
    success_url = reverse_lazy('HomeView')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    def get_context_data(self, *args ,**kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args ,**kwargs)
        

        profile_user=get_object_or_404(Profile, id=self.kwargs['pk'])
        context["profile_user"] = profile_user
        return context

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditUserForm
    template_name = 'registration/edit_user.html'
    success_url = reverse_lazy('HomeView')

    def get_object(self):
        return self.request.user