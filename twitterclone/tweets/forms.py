from django.utils import timezone
from django import forms


class TweetAddForm(forms.Form):
    tweet_text = forms.CharField(max_length=140)
    tweet_time = timezone.now()