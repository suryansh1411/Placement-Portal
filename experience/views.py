from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from experience.forms import ExperienceForm, EffortForm, RoundForm, BookmarkForm
from django.contrib import messages
from . import urls
from .models import Experience, Bookmark
import experience
# Create your views here.


@login_required
def CreateExperience(request):      #function for create experience
    if request.method=='POST':       # request method to get form input
        form=ExperienceForm(request.POST)
        if form.is_valid():                    #if inputs are valid
            experience=form.save(commit=False)
            experience.user=request.user
            experience.save()     # messages.success(request,  "Booking created successfully ")     # url='effort/'+str(experience.id)
            return redirect('experience:create_round', pk=experience.id, n=experience.recruitement_process)
    else:
        form=ExperienceForm()
        return render(request, 'experience/experience_create.html', {'form':form})


@login_required
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
        form=RoundForm()
        return render(request, 'experience/round_create.html', {'form':form})


@login_required
def CreateEffort(request, pk):
    if request.method=='POST':
        form=EffortForm(request.POST)
        if form.is_valid():
            effort=form.save(commit=False)

            exp=get_object_or_404(Experience, pk=pk)
            effort.experience=exp
            effort.save()
            # messages.success(request,  "Booking created successfully ")
            return redirect('home')
    else:
        form=EffortForm()
        return render(request, 'experience/effort_create.html', {'form':form})


###############################################################################################3

@login_required
def BookmarkExperience(request, pk):
    if request.method=='POST':
        form=BookmarkForm(request.POST)
        if form.is_valid():
            bookmark=form.save(commit=False)

            exp=get_object_or_404(Experience, pk=pk)
            bookmark.experience=exp
            bookmark.user=request.user
            bookmark.save()
            # messages.success(request,  "Booking created successfully ")
            return redirect('home')
    else:
        form=BookmarkForm()
        flag=0
        exp=get_object_or_404(Experience, pk)
        aux=Bookmark.objects.all().filter(experience=exp).filter(user=request.user)
        if len(aux)==1:
            flag=1
        else :
            flag=0
        # print(flag+5)
        return render(request, 'experience/effort_create.html', {'form':form, 'flag':flag})
