from django.shortcuts import render, redirect

def index(request):
    return render(request, "mhub/index.html")

def logReg(request):
    return render(request, "mhub/logReg.html")

def processLogin(request):
    return redirect(reverse("go_home"))

def processRegistration(request):
    return redirect(reverse("go_logReg"))

def bio(request):
    return render(request, "mhub/bio.html")

def ping(request):
    print(request.POST['search'])
    return redirect('go_home')

def pong(request):
    return render(request, "mhub/morePongs.html")