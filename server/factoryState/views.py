from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from command.models import Command

from django.utils import timezone

def load(request):
    if FactoryState.objects.exists():
        state=FactoryState.objects[0]
        return render(request, 'loadFactoryState.html', { 'state': state})
    else:
        return HttpResponse("no factory state saved")
