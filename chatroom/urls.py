from django.urls import path
from . import views
# from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


app_name = 'chatroom'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', login_required(views.AboutView.as_view()), name='about'),
    path('register/', views.RegisterView.as_view(), name='user-register'),
    path('profile/', login_required(views.ProfileView.as_view()), name='user-profile'),
    
]