from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from .forms import RegisterForm,LoginForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/main')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {"form":form})


def logout_view(request):
    logout(request)
    return render(request, 'index.html')


def my_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/main')
        else:
            return redirect('/log')
    else:
        form = LoginForm()


    return render(request, 'login.html', {"form":form})
