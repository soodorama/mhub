from django.shortcuts import render, redirect

def index(request):
    return render(request, "mhub/index.html")

def bio(request):
    return render(request, "mhub/bio.html")

def search(request):
    print(request.POST['search'])
    return redirect('home')