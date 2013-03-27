from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from command.models import Command
from factoryState.models import FactoryState
from django.utils import timezone

def command(request):
        if request.method == 'POST':
		_command=request.POST.get('command', 'boo')
		_parameter=request.POST.get('parameter',0)
		_quantity=request.POST.get('quantity',0)
		myCommand = Command(command=_command, statusTimeStamp=timezone.now(), parameter=_parameter, quantity=_quantity, status='queued', commandTimeStamp=timezone.now())
		myCommand.json=jsonTranslation(myCommand)
		if myCommand.command=="placePanel":
			myCommand.description=buildDescription(myCommand)
                myCommand.save()
                return HttpResponse("yo")
	else:
		return HttpResponse("bite me")

def buildDescription(_command):
	if FactoryState.objects.exists():  #assuming we have a factoryState object, pass it to the appropriate json template, render the template, and pass it back, to get stored along with the command
		factoryState=FactoryState.objects.get(id=1)
		description=render_to_string("panelDescription.html", {'command': _command, 'factoryState' : factoryState})
	else:
		description="aaa"
	return description

def jsonTranslation(_command):
	if FactoryState.objects.exists():  #assuming we have a factoryState object, pass it to the appropriate json template, render the template, and pass it back, to get stored along with the command
		factoryState=FactoryState.objects.get(id=1)
		jsonString=render_to_string(_command.command + ".html", {'command': _command, 'factoryState' : factoryState})
	else:
		jsonString=""
	return jsonString

def json(request):
	_command="placeSolette"
	if FactoryState.objects.exists():  #assuming we have a factoryState object, pass it to the appropriate json template, render the template, and pass it back, to get stored along with the command
		factoryState=FactoryState.objects.get(id=1)
		jsonString=render_to_string(_command + ".html", {'command': _command, 'factoryState' : factoryState})
	else:
		jsonString=""
	responseString=_command+" "+jsonString
	return HttpResponse(responseString)

def latestCommand(request):
	return HttpResponse("bluh")

def tinyGParameter(request):
        if request.method == 'POST':
		_command=request.POST.get('command', 'boo')
		_parameter=request.POST.get('parameter',0)
		factoryState=FactoryState.objects.get(id=1)
		if _command.find('var_')!=-1:
			setattr(factoryState, _command, _parameter)
			_command=_command[4:]
			factoryState.save()
		myCommand = Command(command=_command, statusTimeStamp=timezone.now(), quantity=0,parameter=_parameter, status='queued', commandTimeStamp=timezone.now())
		myCommand.json=render_to_string("parameter.html", {'command': myCommand})
                myCommand.save()
                return HttpResponse("parameter set")
	else:
		return HttpResponse("poo")

def factoryState(request):
        if request.method == 'POST':
		_command=request.POST.get('command', 'boo')
		_parameter=request.POST.get('parameter',0)
		factoryState=FactoryState.objects.get(id=1)
		setattr(factoryState, _command, _parameter)
		factoryState.save()
		return HttpResponse("factory settings updated")
	else:
		return HttpResponse("poo")

def newCommands(request):
	if Command.objects.filter(status='queued').order_by('-commandTimeStamp').exists():
		latestCommands=Command.objects.filter(status='queued').order_by('-commandTimeStamp')
		for command in latestCommands:
			command.status= "loaded onto pi"
			command.statusTimeStamp=timezone.now()
			command.save()
		return render(request, 'newCommands.html', { 'commands': latestCommands})
	else:
		return HttpResponse("queue_empty")

def interface(request):
	if FactoryState.objects.exists():  #assuming we have a factoryState object, pass it to the appropriate json template, render the template, and pass it back, to get stored along with the command
		factoryState=FactoryState.objects.get(id=1)
	return render(request, 'interface.html', {'factoryState' : factoryState})

def testing(request):
	if FactoryState.objects.exists():  #assuming we have a factoryState object, pass it to the appropriate json template, render the template, and pass it back, to get stored along with the command
		factoryState=FactoryState.objects.get(id=1)
	return render(request, 'testing.html', {'factoryState' : factoryState})

def startup(request):
	if FactoryState.objects.exists():  #assuming we have a factoryState object, pass it to the appropriate json template, render the template, and pass it back, to get stored along with the command
		factoryState=FactoryState.objects.get(id=1)
	return render(request, 'startup.html', {'factoryState' : factoryState})
