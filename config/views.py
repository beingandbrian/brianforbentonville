from django.shortcuts import render, redirect


def home(request):
    context = dict()
    return render(request, "home.html", context)
