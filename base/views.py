from django.shortcuts import render
from .models import User, Event, Submission
from django.shortcuts import get_object_or_404


# Create your views here.

def home_page(request):
    users = User.objects.filter(event_participant=True)
    events = Event.objects.all()
    context = {'users':users, 'events':events}
    return render(request, 'home.html', context)


def event_page(request, pk):
    event = get_object_or_404(Event, id=pk)
    context = {'event':event}
    return render(request, 'event.html', context)

