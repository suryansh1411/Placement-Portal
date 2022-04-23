from sre_constants import BRANCH
from django import forms
from django.contrib.auth.models import User
from .models import PROGRAMME, YEAR, UserProfile


BRANCH=[
    ('Computer Science and Engineering', 'CSE'),
    ('Mathematics and Computing', 'MNC'),
    ('Electrical and Electronics Engineering', 'EEE'),
    ('Electronics and Communication Engineering', 'ECE'),
    ('Mechanical Engineering', 'ME'),
    ('Engineering Physics', 'EP'),
    ('Data Science and Artificial Intelligence', 'DSAI'),
    ('Chemical Engineering', 'CL'),
    ('Chemical Science and Technology', 'CST'),
    ('Biosciences and Bioengineering', 'BSBE'),

]

YEAR=[
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022')
]

PROGRAMME=[
    ('B. Tech.', '  B. Tech.'),
    ('M. Tech.', 'M. Tech.'),
    ('Ph. D.', 'Ph. D.')
]

def emailcheck(value):
    if(value[-11::]!='@iitg.ac.in'):
        raise forms.ValidationError("You must use E-mail ID provided by IIT-Guwahati.")

class UserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'E-mail ID'}), validators=[emailcheck])
    class Meta():
        model=User
        fields=('username','email','password')


class UserProfileForm(forms.ModelForm):
    branch=forms.ChoiceField(required=True, choices=BRANCH)
    graduation_year=forms.ChoiceField(required=True, choices=YEAR)
    programme=forms.ChoiceField(required=True, choices=PROGRAMME)
    linkedin=forms.CharField(required=False, label="Linkedin User ID")
    github=forms.CharField(required=False, label="Github User ID")

    class Meta():
         model=UserProfile
         fields=('branch', 'graduation_year', 'programme', 'linkedin', 'github')  
        