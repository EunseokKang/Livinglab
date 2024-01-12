# bell_system/views.py

from django.shortcuts import get_object_or_404, render
from .models import BusRoute

def index(request):
    routes = BusRoute.objects.all()
    return render(request, 'bell_system/index.html', {'routes': routes})

def detail(request, route_id):
    route = get_object_or_404(BusRoute, pk=route_id)
    return render(request, 'bell_system/detail.html', {'route': route})
