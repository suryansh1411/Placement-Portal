from unicodedata import name
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from experience.forms import ExperienceForm, EffortForm, RoundForm, BookmarkForm, SearchForm
from django.contrib import messages
from . import urls
from .models import Experience, Bookmark
import experience
from django.contrib.auth.models import User
# Create your views here.


@login_required
# Main function invoked to handle Experience Creation for the website
def CreateExperience(request):      
    if request.method=='POST':      # When the Experience Creation form is filled
        form=ExperienceForm(request.POST)
        if form.is_valid():                    # If the form is filled as expected
            experience=form.save(commit=False)
            experience.user=request.user
            experience.save()       # Save the Experience to the database
            return redirect('experience:create_round', pk=experience.id, n=experience.recruitement_process) 
        else:       # If the form is not filled as expected
            print(form.errors)      
            return render(request, 'experience/experience_create.html', {'form':form})      
    else:
        form=ExperienceForm()
        return render(request, 'experience/experience_create.html', {'form':form})


@login_required
# Function invoked to create
def CreateRound(request, pk, n):
    if request.method=='POST':
        form=RoundForm(request.POST)
        if form.is_valid():
            round=form.save(commit=False)

            exp=get_object_or_404(Experience, pk=pk)
            round.experience=exp
            round.save()
            # messages.success(request,  "Booking created successfully ")
            if n == 1 :
                return redirect('experience:create_effort', pk=pk)
            else :
                return redirect('experience:create_round', pk=pk, n=n-1)
        else:
            print(form.errors)
            return render(request, 'experience/round_create.html', {'form':form})
    else:
        form=RoundForm()
        exp=get_object_or_404(Experience, pk=pk)
        numberOfRounds=exp.recruitement_process-n+1
        return render(request, 'experience/round_create.html', {'form':form, 'numberOfRounds':numberOfRounds})


@login_required
# Function invoked to add Resume and Effort Time to the website
def CreateEffort(request, pk):
    if request.method=='POST':         # If the form is filled as expected
        form=EffortForm(request.POST)
        if form.is_valid():     # If the form is filled as expected
            effort=form.save(commit=False)
            exp=get_object_or_404(Experience, pk=pk)
            effort.experience=exp
            effort.save()       # Save the data to the database
            return redirect('home')
        else:   # If the form is not filled as expected
            print(form.errors)      
    else:   # When the function is called by CreateRound
        form=EffortForm()
        return render(request, 'experience/effort_create.html', {'form':form})


###############################################################################################

@login_required
# Function invoked to Bookmark an Experience
def BookmarkExperience(request, pk):
    if request.method=='POST':  # When the Bookmark button is clicked
        form=BookmarkForm(request.POST)
        if form.is_valid():     # When the button is clicked
            bookmark=form.save(commit=False)    
            exp=get_object_or_404(Experience, pk=pk)
            bookmark.experience=exp
            bookmark.user=request.user
            bookmark.save()     # Save the Bookmarked Profile to the database
            return redirect('home')
        else:   # Invalid request
            print(form.errors)
    else:   # When the Bookmarks page is called
        form=BookmarkForm()
        return render(request, 'experience/effort_create.html', {'form':form})

#################################################################################################

@login_required
def SearchExperience(request):
    if request.method=='POST':
        form=SearchForm(request.POST.dict())
        if form.is_valid():
            data=form.cleaned_data
            pattern=data['pattern']

            context={}
    
            context['experiences']=getExperiences(request, pattern)
            context['form']=BookmarkForm()
            context['searchform']=SearchForm()
            context['searchvalue']=pattern
            return render(request, 'experience/home.html', context)
        else:
            print(form.errors)
            return redirect('home')
    else:
        form=SearchForm
        return redirect('home')


def getExperiences(request,pattern):
    companywise_experiences=Experience.objects.all().filter(company__icontains=pattern)
    namewise_experiences=[]

    users_list=User.objects.all().filter(username__icontains=pattern)

    for user in users_list:
        for exp in user.experiences.all():
            namewise_experiences.append(exp)
        print(user.username)

    experiences=list(set(companywise_experiences) | set(namewise_experiences))

    flag=[]
    for exp in experiences:
        aux=Bookmark.objects.all().filter(experience=exp).filter(user=request.user)
        if len(aux) == 0:
            flag.append(0)
        else :
            flag.append(1)
    return zip(experiences, flag)