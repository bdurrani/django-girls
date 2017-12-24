from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Elvis

@login_required
def unit_list(request):
    units = Elvis.objects.all()
    current_user = request.user
    # import pdb; pdb.set_trace()
    return render(request, 'checkout/unit_list.html', 
    {'units': units, 'inuse': Elvis.IN_USE})
    
@login_required
def update_availability(request):
    # import pdb; pdb.set_trace() 
    units = Elvis.objects.all()
    unitid = request.POST.get('unitid')
    userid = request.POST.get('userid')
    unit = Elvis.objects.get(id=unitid)
    user = User.objects.get(id=userid)
    if(unit.current_user == user):
        checkin_device(unit)
    else:
        checkout_device(unit, user)
    unit.save()
    return HttpResponseRedirect(reverse('unit_list')) 
    
    
def checkin_device(unit):
    unit.current_user = None
    unit.availability = Elvis.AVAILABLE

def checkout_device(unit, user):
  unit.current_user = user
  unit.availability = Elvis.IN_USE

