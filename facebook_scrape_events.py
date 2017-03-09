import urllib.request
import json
import datetime
import time

app_id = "197134180771589"
app_secret = "28a3eaf06aa029934eb3e136e49fdf01" # DO NOT SHARE WITH ANYONE!
page_id = "TrooperRocks"

access_token = app_id + "|" + app_secret

def request_until_succeed(url):
    req = urllib.request.Request(url)
    success = False
    while success is False:
        try:
            response = urllib.request.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)

            print("Error for URL %s: %s" % (url, datetime.datetime.now()))
            print("Retrying.")

    return response.read().decode(response.headers.get_content_charset())

def scrapeFacebookEvents(page_id):
    # Construct the URL string; see http://stackoverflow.com/a/37239851 for
    # Reactions parameters
    url = 'https://graph.facebook.com/v2.6/'+page_id+'/events?access_token='+access_token

    # retrieve data
    #data = json.loads(request_until_succeed(url))

    return request_until_succeed(url)
