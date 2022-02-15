from django.shortcuts import render,redirect    #UserCreationForm,
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import UserRegisterForm
from contactapp.models import Appointment

from django.contrib.auth.forms import AuthenticationForm     #UserCreationForm,
from django.contrib.auth import login,logout
from .forms import UserRegisterForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login')
def account(request):
    # my_profile = Appointment.objects.all()
    my_profile = Appointment.objects.filter(patient=request.user)
    return render(request,'accounts/account.html',{'my_profile':my_profile})




# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('homeapp:homepage')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has created ! You are now able to log in')
            return redirect ('accounts:login')
        else:
            print(form.errors)
    else:
        form =UserRegisterForm()
    return render (request,'accounts/signup.html',{'form':form})

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('homeapp:homepage')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})



def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:logout')
    return render(request,'accounts/logout.html')













