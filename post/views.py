import tweepy

from django.conf import settings #so that I can use the constants from the settings.py file
from django.shortcuts import render, redirect

#This view will be used for posting tweets
def index(request): 
	if request.method == 'POST':
		content = request.POST.get('content', '')

		if content:
			print('Content: ', content)

			auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
			auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

			api = tweepy.API(auth)
			media = api.media_upload("post/image.png")
			api.update_status(status=content, media_ids=[media.media_id])

			return redirect('index')

	return render(request, 'post/index.html')
