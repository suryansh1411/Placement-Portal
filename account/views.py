from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from urllib3 import HTTPResponse
from .forms import UserProfileForm, UserForm
from django.views.generic import DetailView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.models import User
from account.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

def SignupView(request):
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        if(user_form.is_valid() and profile_form.is_valid()):
            user=user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            username=user_form.cleaned_data['username']
            password=user_form.cleaned_data['password']

            profile=profile_form.save(commit=False)
            profile.user=user

            profile.save()

            user=authenticate(username=username , password=password)
            login(request, user)
            
            messages.success(request,  "You were successfully signed-in")
            return redirect('home')

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render(request, 'account/signup.html', {'user_form':user_form,'profile_form':profile_form})



11