# Create your models here.

from sre_constants import BRANCH
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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
    ('2022', '2022'),
    ('2023', '2023')
]

PROGRAMME=[
    ('B. Tech.', 'B. Tech'),
    ('M. Tech.', 'M. Tech'),
    ('Ph. D.', 'Ph. D.')
]

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    branch=models.CharField(blank=False, max_length=50 ,choices=BRANCH)
    graduation_year=models.CharField(blank=False, max_length=50, choices=YEAR)
    programme=models.CharField(blank=False, max_length=50, choices=PROGRAMME)
    linkedin=models.CharField(blank=True, max_length=200)
    github=models.CharField(blank=True, max_length=200)

