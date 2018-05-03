#2) Develop a simple RSS reader. The interface is a web page that accepts an RSS URL and
#lays it out on a web page in a simple but visually appealing manner.

#* User signup and login needed.
#* UI to enter RSS link and show RSS results in same page.

#You can use the following feed for testing purposes
#http://feeds.bbci.co.uk/news/rss.xml

import feedparser

requestUrl = 'http://feeds.bbci.co.uk/news/rss.xml '
r = feedparser.parse(requestUrl)
feed = []
if len(r['entries']) == 0:
    feed.append(['Invalid URL!','',''])
else:
    for i in range(0,len(r['entries'])):
        feed.append([r['entries'][i]['title'],r['entries'][i]['description'],r['entries'][i]['link']])

print(feed)
print(len(feed))
print([feed[0][0]])
print(r['entries'])
print(r.headers)
