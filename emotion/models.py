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
        ('Ax', 'Anxious'),  # thanks to hiren  :P  lol
        ('Wo', 'Worried'),
        ('Fr', 'Frightened'),
    )
    state = models.CharField(max_length=2, choices=emotion_option)
    reason = models.CharField(max_length=1000, null=True, blank=True)
    _date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
