from django.urls import URLPattern, path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

app_name='account'

urlpatterns=[
    path('signup/', views.SignupView, name='user_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
    # path('hi/', views.Hi, name='hi'),
]