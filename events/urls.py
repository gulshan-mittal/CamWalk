from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', views.counter, name='counter'),
    url(r'signup', views.signup, name='signup'),
    url(r'index', views.index, name='signup-login page'),
    url(r'register', views.register, name='register'),
    url(r'success', views.success, name='success page'),
    url(r'login$', views.login, name='login'),
    url(r'create$', views.eventdetails, name='Form for event details'),
    url(r'camera-details$', views.cameradetails, name='Form for camera details'),
]