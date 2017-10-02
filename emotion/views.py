from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from .models import Emotion
from .forms import EmotionForm
import datetime
from django.http import JsonResponse
import calendar
from django.http import HttpRequest
from django.shortcuts import get_object_or_404


def login(request):
    """
    Handle authentication
    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username/Password is not valid!')
            return redirect('/')
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'login.html')


@login_required
def dashboard(request):
    """
    Just return emotion selection option
    :param request:
    :return:
    """
    emotions = Emotion.emotion_option
    return render(request, 'dashboard.html', {'emotions': emotions})


@login_required
def emotion_save(request, key=None):
    """
    Save emotion or serve emotion form by type
    :param request:
    :param key:
    :return:
    """
    if request.method == 'GET':
        _date = datetime.datetime.now().strftime("%m/%d/%Y")
        emotion = dict(Emotion.emotion_option)[key]
        return render(request, 'emotion_save.html', {'key': key, 'emotion': emotion, 'date': _date})
    elif request.method == 'POST':
        form = EmotionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'Form Saved !')
            except Exception as e:
                messages.error(request, e)
        else:
            messages.error(request, form.errors)
        return redirect('emotion', key=request.POST.get('state'))


@login_required
def chart(request):
    """
    Return all emotion count of current year
    :param request:
    :return:
    """
    if request.META.get('HTTP_ACCEPT').startswith("text/html"): # last commit for 2016 :')  bye bye 2k16
        return render(request, 'chart.html')
    elif request.content_type == 'application/json':
        data = []
        today = datetime.datetime.now()
        for emotion in Emotion.emotion_option:
            months = []
            for hiren in range(1, 13):
                single_month = Emotion.objects.filter(created_at__year=today.year, created_at__month=hiren,
                                                      state=emotion[0]).count()
                months.append(single_month)
            temp = {'name': emotion[1], 'data': months}
            data.append(temp)
        return JsonResponse(data, safe=False)


@login_required
def list(request):
    """
    Render list of emotions
    :param request:
    :return:
    """
    if request.method == 'POST':
        month = request.POST.get('month')
        year = request.POST.get('year')
        emotions = Emotion.objects.filter(created_at__month=month, created_at__year=year)
        return render(request, 'list.html', {'month': calendar.month_name[int(month)],
                                             'year': year, 'emotions': emotions})
    today = datetime.datetime.now()
    emotions = Emotion.objects.filter(created_at__month=today.month)
    return render(request, 'list.html', {'month': today.strftime('%B'), 'year': today.year,
                                         'emotions': emotions})
