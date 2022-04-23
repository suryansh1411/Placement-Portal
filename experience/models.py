from django.db import models
from django.contrib.auth.models import User

import experience

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

# Create your models here.
class Experience(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences', null=False)
    company=models.CharField(max_length=50, blank=False, null=False)
    experience_type=models.CharField(max_length=30, blank=False, choices=EXTYPE)
    recruitement_process=models.IntegerField(blank=False)

class Round(models.Model):
    experience=models.ForeignKey(Experience, on_delete=models.CASCADE, null=False)
    type=models.CharField(max_length=100, choices=RTYPE, blank=True)
    description=models.CharField(max_length=500, null=True, blank=True)

class Effort(models.Model):
    experience=models.OneToOneField(Experience, on_delete=models.CASCADE, null=False)
    resume=models.FileField(upload_to=None, null=True, blank=True )
    resources=models.CharField(max_length=100, null=True, blank=True)
    efforts=models.CharField(max_length=100, null=True, blank=True)
    tips=models.CharField(max_length=500, blank=True, null=True)




class Bookmark(models.Model):
    experience=models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='bookmarks')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='userbookmarks')
