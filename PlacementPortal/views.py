from django.shortcuts import render , redirect
from django.views.generic import ListView, TemplateView
from experience.models import Experience, Bookmark
from experience.forms import BookmarkForm, SearchForm

def Home(request):
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


def Profile(request):
    return redirect('home')