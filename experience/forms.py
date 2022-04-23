from dataclasses import field
from django import forms
from .models import EXTYPE, RTYPE, Experience, Effort, Round, Bookmark

EXTYPE=[
    ('Placement', 'Placement'),
    ('Intern', 'Intern'),
    ('Scholarship', 'Scholarship')
]

RTYPE=[
    ('Coding', 'Coding'),
    ('Group Discussion', 'Group Discussion'),
    ('Technical Round', 'Technical Round'),
    ('HR Round', 'HR Round'),
    ('Managerial Round', 'Managerial Round'),
]

def numOfRoundsCheck(value):
    if(value<=0):
        raise forms.ValidationError("Number of Rounds must be greater than 0.")


class ExperienceForm(forms.ModelForm):
    company=forms.CharField()
    experience_type=forms.ChoiceField(required=True, choices=EXTYPE)
    recruitement_process=forms.IntegerField(label="Number of Rounds", validators=[numOfRoundsCheck])

    class Meta():
        model=Experience
        fields=['company', 'experience_type', 'recruitement_process']
       

# def formatOfResume(value):
#     import os
#     ext = os.path.splitext(value.name)[1]
#     valid_extensions = ['.pdf']
#     if not ext.lower() in valid_extensions:
#         raise forms.ValidationError("Resume must be a pdf file.")


class EffortForm(forms.ModelForm):
    resume=forms.FileField(required=False, widget=forms.FileInput(attrs={'accept':'application/pdf'}))
    resources=forms.CharField(widget=forms.Textarea, required=False)
    efforts=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'hh hrs / day'}), required=False)
    tips=forms.CharField(widget=forms.Textarea, required=False)

    class Meta():
        model=Effort
        fields=['resume', 'resources', 'efforts', 'tips']


class RoundForm(forms.ModelForm):
    type=forms.ChoiceField(required=True, choices=RTYPE)
    description=forms.CharField(widget=forms.Textarea, required=False)

    class Meta():
        model=Round
        fields=['type', 'description']



class BookmarkForm(forms.ModelForm):

    class Meta():
        model=Bookmark
        fields=[]
        # fields=['experience', 'user']



