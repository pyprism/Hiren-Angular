from django.forms import ModelForm
from .models import Emotion


class EmotionForm(ModelForm):
    class Meta:
        model = Emotion
        fields = ['state', 'reason', '_date']
