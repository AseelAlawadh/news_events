from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Events
from django.utils import timezone


# def home(request):
#     event = Events.objects
#     return render(request, 'news/home.html', {'event': event})


@login_required(login_url='/accounts/signup')
def create_event(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['location'] and request.POST['create_date'] and request.FILES['icon'] and \
                request.FILES['image']:
            event = Events()
            event.title = request.POST['title']
            event.body = request.POST['body']
            event.location = request.POST['location']
            event.create_date = request.POST['create_date']
            print(event.create_date)
            event.icon = request.FILES['icon']
            event.image = request.FILES['image']
            event.pub_date = timezone.datetime.now()
            # news.votes_total = 1
            event.user_add = request.user
            event.save()
            return redirect('/events/' + str(event.id))
        else:
            return render(request, 'events/create_event.html')

    else:
        return render(request, 'events/create_event.html', {'error': 'all fields required'})


def detail_event(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    return render(request, 'events/detail_event.html', {'event': event})


@login_required(login_url='/accounts/signup')
def coming(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Events, pk=event_id)
        event.coming_total += 1
        event.save()
        return redirect('/events/' + str(event_id))
