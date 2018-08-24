from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import *

def index(request):
    if 'id' in request.session:
        return render(request, "mhub/index.html")
    else:
        return redirect(reverse('go_logReg'))

def logReg(request):
    if 'id' in request.session:
        return redirect(reverse('go_home'))
    return render(request, "mhub/logReg.html")

def processLogin(request):
    errors = User.objects.login_validator(request.POST)
    if 'loginsuccess' in errors:
        request.session['id'] = errors['loginsuccess'].values()[0]['id']
        return redirect(reverse("go_home"))
    else:
        for key,values in errors.items():
            messages.error(request,value,extra_tags=key)
            return redirect(reverse("go_login"))

def processRegistration(request):
    errors = User.objects.registration_validator(request.POST)
    if 'success' in errors:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'] , email_address=request.POST['email_address'] , password=request.POST['password'])
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
    else:
        for key,value in errors.items():
            messages.error(request,value, extra_tags=key)
    return redirect(reverse("go_logReg"))

def bio(request):
    return render(request, "mhub/bio.html")

def ping(request):
    return redirect('go_home')

def save_vid(request):
    # print(request.POST['video_id'])
    # request.session['video_id'] = request.POST['video_id']
    user = User.objects.get(id=request.session['id'])
    video = Video.objects.create(video_name=request.POST['video_name'],video_id=request.POST['video_id'])
    # print(video)
    video.saved_by.add(user)
    return redirect(reverse('go_home'))

def morePong(request):
    if 'id' in request.session: 
        saved_user=User.objects.get(id=request.session['id'])
        return render(request, "mhub/myPongs.html", { "paddle" : Video.objects.filter(saved_by=saved_user)})
    else:
        return redirect(reverse('go_logReg'))

def delete(request, id):
    temp = Video.objects.get(id=id).delete()
    return redirect(reverse('go_morePong'))

def processLogout(request):
    request.session.clear()
    return redirect(reverse('go_logReg'))