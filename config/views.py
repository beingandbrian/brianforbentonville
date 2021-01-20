from django.shortcuts import render, redirect


def home(request):
    context = dict()
    return render(request, "home.html", context)


def contact(request):
    context = dict()
    return render(request, "pages/contact.html", context)
