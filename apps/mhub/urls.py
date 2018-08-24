from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='go_home'),
    url(r'^bio$', views.bio, name='go_bio'),
    url(r'^ping$', views.ping, name='process_pings'),
    url(r'^logReg$', views.logReg, name='go_logReg'),
    url(r'^process/login$', views.processLogin, name='process_login'),
    url(r'^process/registration$', views.processRegistration, name='process_regis'),
    url(r'^save_vid$', views.save_vid, name='save_vid'),
    url(r'^morePong$', views.morePong, name='go_morePong'),
    url(r'^deletePong/(?P<id>\d+)$', views.delete, name='deletePong'),
    url(r'^process/logout$', views.processLogout, name='process_logout'),
]