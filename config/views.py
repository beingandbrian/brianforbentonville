from django.shortcuts import render, redirect


def home(request):
    context = dict()
    return render(request, "home.html", context)


def contact(request):
    context = dict()
    context['uri'] = 'contact'
    return render(request, "pages/contact.html", context)


def gallery(request):
    context = dict()
    context['uri'] = 'photos'
    return render(request, "pages/gallery.html", context)
