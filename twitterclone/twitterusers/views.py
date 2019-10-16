from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

from twitterclone.twitterusers.forms import SignupForm
from django.views import View


# @login_required
# def homepage(request):
#     html = "homepage.html"
#     # tweet = Tweet.objects.order_by(Tweet.tweet_time)
#     # list_of_tweets = tweet.objects.filter(following=True) | Tweet.objects.filter(request.user.twitterusers)
#     list_of_tweets = Tweet.objects.filter(tweet_by=request.user.twitteruser)
#     return render(request, html, {'data': list_of_tweets})


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

@method_decorator(login_required, name='dispatch')
class Homepage(View):
    def get(self, request):
        html = "homepage.html"
        list_of_tweets = Tweet.objects.filter(tweet_by=request.user.twitteruser)
        all_users = TwitterUser.objects.all()
        return render(request, html, {'data': list_of_tweets, 'all_users': all_users})
        

@method_decorator(login_required, name='dispatch')
class Following(View):
    def get(self, request, username):
        following = False
        # we need the instance of the twitteruser
        name = TwitterUser.objects.filter(tag=username)
        following_user = TwitterUser.objects.filter(following=name)
        u = TwitterUser.objects.filter(following=request.user.twitteruser[0])

        if following_user not in u.following:
            u.following.add(following_user)
            following = True
        else:
            u.following.remove(following_user)
            following = False
        u.save()
        return redirect(f'/{username}/')

class ViewOtherProfiles(View):
    def get(self, request, username):
        u = TwitterUser.objects.filter(username=username)
        tweets = Tweet.objects.filter(username_id=u)
        user = TwitterUser.objects.filter(following=request.user.twitteruser)
        count_follows = u.following.count()
        all_followers = u.following.all()
        return render(request, 'viewotherprofiles.html', {'u': u, 'tweets': tweets, 'user': user, 'count_follows': count_follows, 'all_followers': all_followers})



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


# logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))