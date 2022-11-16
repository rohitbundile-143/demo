from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import SignupForm,loginform
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Brainwork

# @csrf_exempt
def home1(request):
    return render(request,'home.html')


def About1(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def dashboard(request):
    if request.user.is_authenticated:
        f2=Brainwork.objects.all()
        return render(request,'dash.html',{'form':f2})

    else:
     return HttpResponseRedirect('/logout1/')




def logout1(request):
    logout(request)
    return HttpResponseRedirect('/')



def signup(request):
    # pi=SignupForm()
    if request.method =='POST':
        pi=SignupForm(request.POST)
        if pi.is_valid():
           messages.success(request,'Congratulations!! Your Registrations Are Success')
           pi.save()

    else:
        pi=SignupForm()
    return render(request,'signup.html',{'form':pi})


def login1(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            first=loginform(request=request,data=request.POST)
            if first.is_valid():
               uname = first.cleaned_data['username']
               upass = first.cleaned_data['password']
               user = authenticate(username=uname,password=upass)
               if user is not None:           #suppose user allerady register so that time you have authority to logine
                   login(request,user)
                   messages.success(request,'logged in Successfully')
                   return HttpResponseRedirect('/dash/')
        else:
                first = loginform()
        return render(request,'login.html',{'form':first})
    else:
        return HttpResponseRedirect('/dash/')

