from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', views.counter, name='counter'),
    url(r'^$', views.analysis1, name='analysis1'),
]