from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
def analysis1(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return render(request, 'analysis/analysis1.html', {})
