from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
def counter(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return render(request, 'crowdcounter/crowdcount.html', {})