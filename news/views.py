from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import News
from django.utils import timezone


# Create your views here.

def home(request):
    news = News.objects
    return render(request, 'news/home.html', {'news': news})


@login_required(login_url='/accounts/signup')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES[
            'icon'] and request.FILES['image']:
            news = News()
            news.title = request.POST['title']
            news.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith(
                    'https://'):
                news.url = request.POST['url']
            else:
                news.url = 'http://' + request.POST['url']

            news.icon = request.FILES['icon']
            news.image = request.FILES['image']
            news.pub_date = timezone.datetime.now()
            # news.votes_total = 1
            news.user_add = request.user
            news.save()
            return redirect('/news/' + str(news.id))
        else:
            return render(request, 'news/create.html')

    else:
        return render(request, 'news/create.html', {'error': 'all fields required'})


def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/detail.html', {'news': news})


@login_required(login_url='/accounts/signup')
def upvote(request, news_id):
    if request.method == 'POST':
        news = get_object_or_404(News, pk=news_id)
        news.votes_total += 1
        news.save()
        return redirect('/news/' + str(news_id))
