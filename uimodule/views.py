from django.shortcuts import render
from django.utils import timezone
from .models import Satellite

# Create your views here.
def ui(request):
    satellites = Satellite.objects.filter(updated_time__lte=timezone.now()).order_by('updated_time')
    return render(request, 'uimodule/Satellite.html',{'satellites':satellites})
