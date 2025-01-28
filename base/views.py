from django.shortcuts import render
from .models import User, Event, Submission

# Create your views here.

def home_page(request):
    users = User.objects.filter(event_participant=True)
    context = {'users':users}
    return render(request, 'home.html', context)
