from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from experience.forms import ExperienceForm, EffortForm, RoundForm, BookmarkForm, SearchForm
from django.contrib import messages
from . import urls
from .models import Experience, Bookmark
import experience
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
            print(form.errors)
    else:
        form=EffortForm()
        return render(request, 'experience/effort_create.html', {'form':form})


###############################################################################################

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
            print(form.errors)
    else:
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
            experiences=Experience.objects.all()
    
            flag=[]
            for exp in experiences:
                aux=Bookmark.objects.all().filter(experience=exp).filter(user=request.user)
                if len(aux) == 0:
                    flag.append(0)
                else :
                    flag.append(1)

            context['experiences']=zip(experiences, flag)
            context['form']=BookmarkForm()
            context['searchform']=SearchForm()
            return render(request, 'experience/home.html', context)
        else:
            print(form.errors)
            return redirect('home')
    else:
        form=SearchForm
        return redirect('home')
