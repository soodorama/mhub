from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def index(request):
    return render(request, "mhub/index.html")

def bio(request):
    return render(request, "mhub/bio.html")

def search(request):
    return redirect(reverse('home'))