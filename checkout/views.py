from django.shortcuts import render
from .models import Elvis
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

@login_required
def unit_list(request):
    units = Elvis.objects.all()
    current_user = request.user
    print('hit unit_list %s' % (request.method))
    # import pdb; pdb.set_trace()
    return render(request, 'checkout/unit_list.html', 
    {'units': units, 'inuse': Elvis.IN_USE})
    
def update_availability1(request):
    unitid = -1
    userid = -1
    # import pdb; pdb.set_trace() 
    if request.method == "POST":
        units = Elvis.objects.all()
        print("This was a POST")
        unitid = request.POST.get('unitid')
        userid = request.POST.get('userid')
        unit = Elvis.objects.get(id=unitid)
        user = User.objects.get(id=userid)
        if(unit.current_user == user):
            print('user already reserved the device. Check in device')
            checkin_device(unit)
        else:
            print('checking out device')
            checkout_device(unit, user)
        unit.save()
        return HttpResponseRedirect('/checkout')
        # return render(request, 'checkout/unit_list.html',  {'units': units, 'inuse': Elvis.IN_USE})
        
    print('This was a GET')
    unitid = request.GET['unitid']
    userid = request.GET['userid']
        
    print('update_availability userid: %s unit_id: %s' % (userid, unitid))
    user = User.objects.get(id=userid)
    unit = Elvis.objects.get(id=unitid)
    operation = 'checkin'
    if(unit.current_user == user):
        print('user already reserved the device. Check in device')
        checkin_device(unit)
    else:
        print('checking out device')
        checkout_device(unit, user)
        operation = 'checkout'
    unit.save()
    print('current user %s' % unit.current_user)
    return JsonResponse( {
        'unitid':unitid,
        'operation': operation ,
        'availability': unit.get_availability_display(),
        'username': user.username
        })
    # return HttpResponse(status=204) 
    
    
# def update_availability(request, pk, userid):
#     return HttpResponse(status=204) 
#     user = User.objects.get(id=userid)
#     unit = Elvis.objects.get(id=pk)
#     # import pdb; pdb.set_trace()
#     if(unit.current_user == user):
#         print('user already reserved the device')
#         unit.current_user = None
#         unit.availability = Elvis.AVAILABLE
#     else:
#         print('checking out device')
#         checkout_device(unit, user)
#     unit.save()
#     return HttpResponse(status=204) 
    
def checkin_device(unit):
    unit.current_user = None
    unit.availability = Elvis.AVAILABLE

def checkout_device(unit, user):
  unit.current_user = user
  unit.availability = Elvis.IN_USE

