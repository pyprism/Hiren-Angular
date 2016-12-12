from django.db import models


class Emotion(models.Model):
    emotion_option = (
        ('Sa', 'Sad'),
        ('An', 'Angry'),
        ('Co', 'Confused'),
        ('Ha', 'Happy'),
        ('Ro', 'Romantic'),  # oh really :O
        ('De', 'Depressed'),
        ('Si', 'Sick'),
        ('Ax', 'anxious'),  # thanks to hiren  :P  lol
        ('Wo', 'worried'),
        ('Fr', 'frightening'),
    )
    state = models.CharField(max_length=2, choices=emotion_option)
    reason = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
