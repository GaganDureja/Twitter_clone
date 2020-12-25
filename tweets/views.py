from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Tweet

from .forms import TweetForm

# Create your views here.






def home_view(request, *args, **kwargs):	
	return HttpResponse('<h1>Hello world</h1>')



def tweet_detail_view(request, tweet_id, *args, **kwargs):
	try:
		obj = Tweet.objects.get(id=tweet_id)
	except:
		raise Http404
	return HttpResponse(f'<h1>Hello {tweet_id} - {obj.content}</h1>')
	

def tweet_create_view(request, *args, **kwargs):
	form = TweetForm(request.POST or None)
	if form.is_valid():
		obj= form.save(commit=False)
		obj.save()
		form = TweetForm()
	return render(request, 'components/form.html', context={'form':form})