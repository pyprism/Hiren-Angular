from django.core.urlresolvers import resolve
from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User
from django.test import Client
from .models import Emotion
from . import views
from freezegun import freeze_time


class ModelTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        Emotion.objects.create(state='Sa', reason="test", _date='2016-12-17')

    def test_model_stored_correct_object(self):
        self.assertEqual(Emotion.objects.count(), 1)

        emotion = Emotion.objects.all()
        self.assertEqual(emotion[0].state, 'Sa')


class LoginViewTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        Emotion.objects.create(state='Sa', reason="test", _date='2016-12-17')
        self.c = Client()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'bunny')

    def test_login_url_resolves_to_login_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.login)

    def test_auth_works(self):
        respond = self.c.post('/', {'username': 'hiren', 'password': 'bunny'})
        self.assertRedirects(respond, '/dashboard/')

    def test_redirect_works_for_bad_auth(self):
        respond = self.c.post('/', {'username': 'hiren', 'password': 'bad pass'})
        self.assertRedirects(respond, '/')