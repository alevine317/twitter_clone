"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from twitterclone.authentication import views as auth_views
from twitterclone.tweets import views as tweet_views
from twitterclone.twitterusers import views as twitteruser_views

from twitterclone.tweets.models import Tweet
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.notifications.models import Notifications

admin.site.register(Tweet)
admin.site.register(TwitterUser)
admin.site.register(Notifications)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.login_view, name='index'),
    path('logout/', auth_views.logout_view),
    path('addtweet/', tweet_views.tweet_add),
    path('signup/', twitteruser_views.signup_view),
    path('', twitteruser_views.homepage, name='homepage'),
    path('tweet/<int:id>/', tweet_views.tweet),
    path('twitter_user/<str:username>/', twitteruser_views.profile_view)
]