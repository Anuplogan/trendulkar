from django.shortcuts import render
from django.http import HttpResponse
import twitter


# Create your views here.
def index(request):
#    return HttpResponse("<h1>HELLO I'M ANUPAM<h1/>")
    api = twitter.Api(consumer_key='sBRwxQ7IyVqnJ5ocaNpChU4dl',
                      consumer_secret='PPv9Q7bkJRYo9meiBppehRlyxKBky9S0OMhTTOfSNYvgN5uNTY',
                      access_token_key='2446069779-dIfqCLMukctLuN02WqHsWrNdViGpLm4TTl3qgRR',
                      access_token_secret='0SFk1zUNIfcrULejMEtr8ubyE5Vf7lFQ8TimXq6flkdNL')
    trend = api.GetTrendsWoeid(woeid=23424848)
    return render(request, 'blog/index.html', { 'head': trend})
    