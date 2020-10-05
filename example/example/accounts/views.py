from django.shortcuts import render


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm


@login_required
def index(request):
    return render(request,'accounts/index.html')
def sign_up(request):
    #context = {}
    form = CreateUserForm()
    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

            return render(request,'accounts/index.html')
    context = {'form': form}
    return render(request,'registration/sign_up.html',context)