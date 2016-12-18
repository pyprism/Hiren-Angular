from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from .models import Emotion
from .forms import EmotionForm
import datetime
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
        return redirect(request.META.get('HTTP_REFERER'))


@login_required
def chart(request):
    today = datetime.datetime.now()
    from_this_year = Emotion.objects.filter(created_at__year=today.year)
    return render(request, 'chart.html')
