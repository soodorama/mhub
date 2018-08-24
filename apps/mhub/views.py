from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

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
    return redirect('go_home')

def load_vid(request):
    request.session['video_id'] = request.POST['video_id']
    return redirect('go_home')