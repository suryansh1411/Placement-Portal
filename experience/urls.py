from django.urls import URLPattern, path, re_path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='experience'

urlpatterns=[

    path('experience/', views.CreateExperience, name='create_experience'),
    path('round/<pk>/<int:n>/', views.CreateRound, name='create_round'),
    path('effort/<pk>', views.CreateEffort, name='create_effort'),
    path('bookmark/<pk>', views.BookmarkExperience, name='bookmark_experience'),
    path('search/', views.SearchExperience, name='search_experience'),
]