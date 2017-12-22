from django.shortcuts import render
from .models import Elvis
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

@login_required
def unit_list(request):
    units = Elvis.objects.all()
    current_user = request.user
    # import pdb; pdb.set_trace()
    print (current_user.id)
    return render(request, 'checkout/unit_list.html', {'units': units})
    
def update_availability(request, pk, userid):
    import pdb; pdb.set_trace()
    user = User.objects.get(id=userid)
    unit = Elvis.objects.filter(id=pk)
    unit.current_user = user;
    unit.save()
    return HttpResponse(status=204)

