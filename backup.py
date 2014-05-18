# Backup all your Instagram photos
# by Christopher Su
# May 18, 2014

from instagram.client import InstagramAPI
import sys
import secret
import os
import urllib2
import urlparse

USERNAME = str(sys.argv[1])
downloads_dir = os.path.dirname(os.path.abspath(__file__)) + '/downloads'

access_token = secret.ACCESS_TOKEN
api = InstagramAPI(access_token=access_token)
USER_ID = api.user_search(USERNAME, count=1)[0].id
recent, next = api.user_recent_media(user_id=USER_ID, count=-1)
# recent = recent[0:80] # truncate results if necessary to avoid reaching API limit
for cur in recent[:-1]:
    # print str(cur.images["standard_resolution"].url)
    url = str(cur.images["standard_resolution"].url)
    filename = url.split("/")[-1]
    file_path = os.path.join(downloads_dir, filename)
    if not os.path.isfile(file_path): # don't download something twice
        path = urlparse.urlparse(url).path
        ext = os.path.splitext(path)[1]
        file = urllib2.urlopen(url)
        output = open(os.path.join(file_path),'wb')
        output.write(file.read())
        output.close()
        print 'Downloaded: ' + filename
    else:
        print filename + " was already downloaded."

# maybe change it to use
# import urllib
# urllib.urlretrieve("http://sadfasdfasdf.com//00000001.jpg", "00000001.jpg")
# instead?