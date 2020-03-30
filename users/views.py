from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import Register_form


def register(request):
    if request.method == 'POST':
        form = Register_form(request.POST)
        if form.is_valid():
            form.save()
            context = {"message": "ACCOUNT CREATED"}
            return redirect("users/loginoperator/",context)
    else:
        form = Register_form()

    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and user.is_operator == True:
            login(request, user)
            return HttpResponseRedirect(reverse("first:index"))
        else:
            context["error"] = "Provide Valid Credentials"
            return render(request, "users/login_op.html", context)
    else:
        return render(request, "users/login_op.html", context)


def Manager_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and user.is_manager == True:
            login(request, user)
            return HttpResponseRedirect(reverse("first:p_detail"))
        else:
            context = {"error": "Provide Valid Credentials"}
            return render(request, "users/login_manager.html", context)
    else:
        return render(request, "users/login_manager.html", context)
