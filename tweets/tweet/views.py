from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.


@login_required
def all_tweets(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets.html', {'tweets': tweets})

@login_required
def make_tweets(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()    
            return redirect('all_tweets')
    else:
        form = TweetForm()
    return render(request, 'make_tweet.html', {'form': form})

@login_required
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('all_tweets')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'make_tweet.html', {'form': form})

@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id)
    if request.method == 'POST':
        tweet.delete()
        return redirect('all_tweets')
    return render(request, 'delete_tweet.html', {'tweet': tweet}) 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password (form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('all_tweets')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html',{'form': form})