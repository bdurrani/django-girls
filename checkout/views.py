from django.shortcuts import render
from .models import Elvis

def unit_list(request):
    units = Elvis.objects
    return render(request, 'checkout/unit_list.html', {'units': units})
