from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from order.models import Order, OrderForm
from django.utils import timezone

def order(request):
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                _customerid  =   form.cleaned_data['customerid']
                _voltage     =   form.cleaned_data['voltage']
                _current     =   form.cleaned_data['current']
                _width       =   form.cleaned_data['width']
                _height      =   form.cleaned_data['height']
                _status      =   form.cleaned_data['status']

                job = Order(customerid=_customerid, voltage=_voltage, current=_current, width=_width, height=_height, status=_status, order_ts=timezone.now())
                job.save()

                return HttpResponse("thank you!")
            
            else:
                form = OrderForm()
                render(request, 'order.html', {
                        'form': form,
                        })

        else: 
            form = OrderForm()
            return render(request, 'order.html', {
               'form': form,
               })

def finished(request):
	return render(request, 'finished.html')
