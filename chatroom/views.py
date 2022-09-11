from gettext import install
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm
from django.contrib import messages
# Create your views here.


class IndexView(View):
    def get(self, request):
        # <view logic>
        return render(request, 'chatroom/index.html')


class AboutView(View):

    def get(self, request):
        # <view logic>
        return render(request, 'chatroom/about.html')


class RegisterView(View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'chatroom/register.html', {'form' : form}) 

    def post(self,request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login')
            return redirect('login')


class ProfileView(View):
    
    def get(self, request):
        profile = UserProfileForm(instance = request.user)
        context = { 'form' : profile }
        return render(request, 'chatroom/profile.html', context)
