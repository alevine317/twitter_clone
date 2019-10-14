from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from twitterclone.twitterusers.forms import SignupForm
from django.views import View


# @login_required
# def homepage(request):
#     html = "homepage.html"
#     # tweet = Tweet.objects.order_by(Tweet.tweet_time)
#     # list_of_tweets = tweet.objects.filter(following=True) | Tweet.objects.filter(request.user.twitterusers)
#     list_of_tweets = Tweet.objects.filter(tweet_by=request.user.twitteruser)
#     return render(request, html, {'data': list_of_tweets})


@login_required
class Homepage(View):
    def get(self, request):
        html = "homepage.html"
        list_of_tweets = Tweet.objects.filter(tweet_by=request.user.twitteruser)
        return render(request, html, {'data': list_of_tweets})
        

# def profile_view(request, username):
#     html = 'profile.html'

#     breakpoint()
#     username = TwitterUser.objects.filter(id=id)
#     user_tweets = Tweet.objects.filter(username=username)
#     return render(request, html, {'data': username, 'tweets': user_tweets})

# def signup_view(request):
#     html = "generic_form.html"
#     form = None

#     if request.method == 'POST':
#         form = SignupForm(request.POST)

#         if form.is_valid():
#             data = form.cleaned_data
#             user = User.objects.create_user(username=data['username'], password=data['password'])
#             login(request, user)
#             TwitterUser.objects.create(
#                 tag=data['tag'],
#                 person=user
#             )
#             return HttpResponseRedirect(reverse('homepage'))
#     else:
#         form = SignupForm()
#     return render(request, html, {'form': form})

class ProfileView(View):
    def get(self, request):
        html = 'profile.html'
        username = TwitterUser.objects.filter(id=id)
        user_tweets = Tweet.objects.filter(username=username)
        return render(request, html, {'data': username, 'tweets': user_tweets})

class SignupView(View):
    def post(self, request):
        html = "generic_form.html"
        form = None

        if request.method == 'POST':
            form = SignupForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                user = User.objects.create_user(username=data['username'], password=data['password'])
                login(request, user)
                TwitterUser.objects.create(
                    tag=data['tag'],
                    person=user
                )
                return HttpResponseRedirect(reverse('homepage'))
        else:
            form = SignupForm()
        return render(request, html, {'form': form})

# logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))