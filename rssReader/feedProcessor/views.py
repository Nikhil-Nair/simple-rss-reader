from django.shortcuts import render
from django.http import HttpResponse

import json, feedparser
# Create your views here.
def home(request):
    return render(request, "home.html", {})

def getFeed(request):

    feed = []
    feedurl = request.GET.get('feedURL')
    data = feedparser.parse(feedurl)

    if len(data['entries']) == 0:
        feed.append(['Invalid URL!','',''])
    else:
        for i in range(0,len(data['entries'])):
            feed.append([data['entries'][i]['title'],data['entries'][i]['description'],data['entries'][i]['link'],data['entries'][i]['published']])
    response_data = {"feedData" : feed}

    return HttpResponse(json.dumps(response_data))
