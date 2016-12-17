from django.core.urlresolvers import resolve
from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User
from django.test import Client
from .models import Emotion
from freezegun import freeze_time


class ModelTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        Emotion.objects.create(state='Sa', reason="test", _date='2016-12-17')

    def test_model_stored_correct_object(self):
        self.assertEqual(Emotion.objects.count(), 1)

        emotion = Emotion.objects.all()
        self.assertEqual(emotion[0].state, 'Sa')
